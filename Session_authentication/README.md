<h2>Background Context</h2>
<p>In this project, you will implement a&nbsp;<strong>Session Authentication</strong>. You are not allowed to install any other module.</p>
<p>In the industry, you should&nbsp;<strong>not</strong> implement your own Session authentication system and use a module or framework that doing it for you (like in Python-Flask:&nbsp;<a href="https://intranet.hbtn.io/rltoken/X_Ss7um7S0h2y62_R5U5jQ" title="Flask-HTTPAuth" target="_blank">Flask-HTTPAuth</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
    <li><a href="https://intranet.hbtn.io/rltoken/vyJGpJSSrFRe0LuWasDqCQ" title="REST API Authentication Mechanisms - Only the session auth part" target="_blank">REST API Authentication Mechanisms - Only the session auth part</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/Ry_Fo8MjzSa1KZ2nIijqOA" title="HTTP Cookie" target="_blank">HTTP Cookie</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/V0qd3lJG4kR_kwojoaFZng" title="Flask" target="_blank">Flask</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/sfyvsYn5YM2MDBUqyqnK-A" title="Flask Cookie" target="_blank">Flask Cookie</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.hbtn.io/rltoken/N7kCrbRr7O0pfv8oVVzynw" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
    <li>What authentication means</li>
    <li>What session authentication means</li>
    <li>What Cookies are</li>
    <li>How to send Cookies</li>
    <li>How to parse Cookies</li>
</ul>
<h2>Requirements</h2>
<h3>Python Scripts</h3>
<ul>
    <li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using&nbsp;<code>python3</code> (version 3.7)</li>
    <li>All your files should end with a new line</li>
    <li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/env python3</code></li>
    <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
    <li>Your code should use the&nbsp;<code>pycodestyle</code> style (version 2.5)</li>
    <li>All your files must be executable</li>
    <li>The length of your files will be tested using&nbsp;<code>wc</code></li>
    <li>All your modules should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;</code>)</li>
    <li>All your classes should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&apos;</code>)</li>
    <li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).my_function.__doc__)&apos;</code> and&nbsp;<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&apos;</code>)</li>
    <li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>