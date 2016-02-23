# _*_ coding: utf-8 _*_

'''
Geocoding and Reverse Geocoding

아래의 code은 GSM의 CID, LAC을 사용하여  latitude, longitude을 계산하는 java program이다.
이를 활용하여  python script에서  유사한 기능을 만들 수 있다.
package com.AndroidTelephonyManager;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;
import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.telephony.TelephonyManager;
import android.telephony.gsm.GsmCellLocation;
import android.widget.TextView;

public class AndroidTelephonyManager extends Activity 
{ 
    int myLatitude, myLongitude;
    /** Called when the activity is first created. */  
    
    @Override  public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        TextView textGsmCellLocation = (TextView)findViewById(R.id.gsmcelllocation);
        TextView textCID = (TextView)findViewById(R.id.cid);
        TextView textLAC = (TextView)findViewById(R.id.lac);
        TextView textGeo = (TextView)findViewById(R.id.geo);
        
        //retrieve a reference to an instance of TelephonyManager      
        TelephonyManager telephonyManager = (TelephonyManager)getSystemService(Context.TELEPHONY_SERVICE);
        GsmCellLocation cellLocation = (GsmCellLocation) telephonyManager.getCellLocation();
        int cid = cellLocation.getCid();
        int lac = cellLocation.getLac();
        textGsmCellLocation.setText(cellLocation.toString());
        textCID.setText("gsm cell id: " + String.valueOf(cid));
        textLAC.setText("gsm location area code: " + String.valueOf(lac));
      
        if(RqsLocation(cid, lac))
        {
            textGeo.setText(  String.valueOf((float)myLatitude/1000000)  + " : "  + String.valueOf((float)myLongitude/1000000));
        }
        else
        {       
    
        }      
    }   
    
    private Boolean RqsLocation(int cid, int lac)
    {      
        Boolean result = false;
        String urlmmap = "http://www.google.com/glm/mmap";
        try 
        {       
            URL url = new URL(urlmmap);
            URLConnection conn = url.openConnection();
            HttpURLConnection httpConn = (HttpURLConnection) conn;
            httpConn.setRequestMethod("POST");
            httpConn.setDoOutput(true);
            httpConn.setDoInput(true);
            httpConn.connect();
            OutputStream outputStream = httpConn.getOutputStream();
            WriteData(outputStream, cid, lac);
            InputStream inputStream = httpConn.getInputStream();
            DataInputStream dataInputStream = new DataInputStream(inputStream);
            dataInputStream.readShort();
            dataInputStream.readByte();
            int code = dataInputStream.readInt();
            if (code == 0)
            {         
                myLatitude = dataInputStream.readInt();
                myLongitude = dataInputStream.readInt();
                result = true;
            } 
        } 
        catch (IOException e) 
        {  
            // TODO Auto-generated catch block  e.printStackTrace();
        }  
        return result;
    }

    private void WriteData(OutputStream out, int cid, int lac)  throws IOException  
    {          
        DataOutputStream dataOutputStream = new DataOutputStream(out);
        dataOutputStream.writeShort(21);
        dataOutputStream.writeLong(0);
        dataOutputStream.writeUTF("en");
        dataOutputStream.writeUTF("Android");
        dataOutputStream.writeUTF("1.0");
        dataOutputStream.writeUTF("Web");
        dataOutputStream.writeByte(27);
        dataOutputStream.writeInt(0);
        dataOutputStream.writeInt(0);
        dataOutputStream.writeInt(3);
        dataOutputStream.writeUTF("");
        dataOutputStream.writeInt(cid);
        dataOutputStream.writeInt(lac);
        dataOutputStream.writeInt(0);
        dataOutputStream.writeInt(0);
        dataOutputStream.writeInt(0);
        dataOutputStream.writeInt(0);
        dataOutputStream.flush();
    } 
      
}

'''

