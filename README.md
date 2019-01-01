# autotype
<h2>This script was usedfor code injection onto a computer system for btaining a reverse shell. (Complete code won't be provided for safety purposes)</h2>
<ul>
<li>When delivering a metasplot payload using the traditional method, the payload can be detected by antivirus software and hence get blocked.</li>
<li>To get ppast that, I pasted the contents of the payload into the .py file as a string and made some tweaks to the file.</li>
<li>Then, convert the .py file to a .exe file using a third party tool.</li>
<li>The .exe file was pasted onto a pendrive and the autorun was configured to run it by default.</li>
<li><strong>Now, as soon as the pendrive is plugged-in to the target system, the payload gets typed out onto the terminal without being detected by an antivirus and hence we get a reverse shell.</li>
