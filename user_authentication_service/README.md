<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/12/4cb3c8c607afc1d1582d.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230530%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230530T230832Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8d4730dbc425a2ed1c418efcd8a6e3d10ef46f0b0d8b649f469f93a417be52f0" alt=""></p>
<p>In the industry, you should&nbsp;<strong>not</strong> implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask:&nbsp;<a href="https://intranet.hbtn.io/rltoken/RlAyQIsd3S00AFdTiorEUQ" title="Flask-User" target="_blank">Flask-User</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</p>
<h2>Resources</h2>
<p><strong>Read or watch:</strong></p>
<ul>
    <li><a href="https://intranet.hbtn.io/rltoken/T03S8hNvX_1hXW66qK0Z6w" title="Flask documentation" target="_blank">Flask documentation</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/nf0Y9myaDn6kIJckvB9E4w" title="Requests module" target="_blank">Requests module</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/a_OTic47lD-ZhoWKIGINBw" title="HTTP status codes" target="_blank">HTTP status codes</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.hbtn.io/rltoken/PTIhFapJKLUJ76WnfXonkQ" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<ul>
    <li>How to declare API routes in a Flask app</li>
    <li>How to get and set cookies</li>
    <li>How to retrieve request form data</li>
    <li>How to return various HTTP status codes</li>
</ul>
<h2>Requirements</h2>
<ul>
    <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
    <li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using&nbsp;<code>python3</code> (version 3.7)</li>
    <li>All your files should end with a new line</li>
    <li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/env python3</code></li>
    <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
    <li>Your code should use the&nbsp;<code>pycodestyle</code> style (version 2.5)</li>
    <li>You should use&nbsp;<code>SQLAlchemy</code> 1.3.x</li>
    <li>All your files must be executable</li>
    <li>The length of your files will be tested using&nbsp;<code>wc</code></li>
    <li>All your modules should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;</code>)</li>
    <li>All your classes should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&apos;</code>)</li>
    <li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).my_function.__doc__)&apos;</code> and&nbsp;<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&apos;</code>)</li>
    <li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
    <li>All your functions should be type annotated</li>
    <li>The flask app should only interact with&nbsp;<code>Auth</code> and never with&nbsp;<code>DB</code> directly.</li>
    <li>Only public methods of&nbsp;<code>Auth</code> and&nbsp;<code>DB</code> should be used outside these classes</li>
</ul>
<h2>Setup</h2>
<p>You will need to install&nbsp;<code>bcrypt</code></p>
<pre><code>pip3 install bcrypt</code></pre>