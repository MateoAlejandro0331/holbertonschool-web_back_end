<h2>Background Context</h2>
<p>In this project, you will learn what the authentication process means and implement a&nbsp;<strong>Basic Authentication</strong> on a simple API.</p>
<p>In the industry, you should&nbsp;<strong>not</strong> implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask:&nbsp;<a href="https://intranet.hbtn.io/rltoken/DohDIWawzCz6fgeA1V9dwQ" title="Flask-HTTPAuth" target="_blank">Flask-HTTPAuth</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</p>
<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/5/6ccb363443a8f301bc2bc38d7a08e9650117de7c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230510%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230510T195227Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8eda96d080faa17d76eddc3fa9ff2d7aea22034d4b6881deb9615be21f97fad1" alt=""></p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
    <li><a href="https://intranet.hbtn.io/rltoken/Kb7ELziV7EkpqtPTUXY2ZQ" title="REST API Authentication Mechanisms" target="_blank">REST API Authentication Mechanisms</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/ENKa96b6goJUM4nm_unPqw" title="Base64 in Python" target="_blank">Base64 in Python</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/liL0xdWlzf5sweZyTEc4_w" title="HTTP header Authorization" target="_blank">HTTP header Authorization</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/XTf6irC31_V8bIKKhRE5AA" title="Flask" target="_blank">Flask</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/97wy7KWBzuiVkbKOSDUzng" title="Base64 - concept" target="_blank">Base64 - concept</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.hbtn.io/rltoken/cJmYXZqDAUuOvTffnjeRng" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
    <li>What authentication means</li>
    <li>What Base64 is</li>
    <li>How to encode a string in Base64</li>
    <li>What Basic authentication means</li>
    <li>How to send the Authorization header</li>
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