# WeLeakInfo.to API key Checker
API Key checker for https://weleakinfo.to/ 

![Capture](https://user-images.githubusercontent.com/58238467/155846999-753e0f13-bb75-48df-b69d-36a555d05fea.PNG)

<h2> About the program </h2>
This program will automatically generate API keys for the website WeLeakInfo.to and check them. The website provides leaked info for emails, passwords or usernames, just like other big leaked data
websites like haveibeenpwned.com.

* If you got an API key try requesting this URL <b><p>https://api.weleakinfo.to/api?value={THE EMAIL}&type=email&key={API KEY}</p></b> Replacing 
{THE EMAIL} with the email that you want to get it's leaked passwords and replcae {API KEY} with the API key you got.
  
  
 <h2> How To Use This Tool </h2>
 
 * Note That This tool works on Windows 10 perfectly and I didn't really check it on other OS so it's better to use it on Windows 10.
 
 <h3> This Tool Uses 3 Files</h3>
 
 - the proxy file (whatever u named it)
 - valid_keys.txt
 - tele.txt
 
 First you need a proxy file with HTTP/S or SOCKS4/5 proxies and you can name it whatever you want. Then valid_keys.txt file is the file where all found valid API keys will be stored, 
 it's not really necessary file if you are getting the hits on telegram, you don't have to put anything in the file. The last file is tele.txt where you have to put your telegram
 bot API token and your telegram ID in the file in this format token/id. <b> If you don't want to get the hits on telegram do not forget to change the telegram variable in the source
 code to False so you don't get any errors. </b>
 
