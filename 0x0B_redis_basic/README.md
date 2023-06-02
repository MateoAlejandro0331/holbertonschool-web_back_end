<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/1/40eab4627f1bea7dfe5e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230602%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230602T160558Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5383705c9bb033eea0d48f3bfe7d8f95947070e995210d5e719c91d17414b713" alt=""></p>
<h2>Resources</h2>
<p><strong>Read or watch:</strong></p>
<ul>
    <li><a href="https://intranet.hbtn.io/rltoken/uEy5gRIS2gEb08ZiSP8ANw" title="Redis commands" target="_blank">Redis commands</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/yqIvla14uyQ2pBRk2i-tBQ" title="Redis python client" target="_blank">Redis python client</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/NxpS4PTyCpDK29oLyCBwHQ" title="How to Use Redis With Python" target="_blank">How to Use Redis With Python</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/vk2Wan5dEYyoGNwCIvoFaQ" title="Redis Crash Course Tutorial" target="_blank">Redis Crash Course Tutorial</a></li>
</ul>
<h2>Learning Objectives</h2>
<ul>
    <li>Learn how to use redis for basic operations</li>
    <li>Learn how to use redis as a simple cache</li>
</ul>
<h2>Requirements</h2>
<ul>
    <li>All of your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)</li>
    <li>All of your files should end with a new line</li>
    <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
    <li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/env python3</code></li>
    <li>Your code should use the&nbsp;<code>pycodestyle</code> style (version 2.5)</li>
    <li>All your modules should have documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;</code>)</li>
    <li>All your classes should have documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&apos;</code>)</li>
    <li>All your functions and methods should have documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).my_function.__doc__)&apos;</code> and&nbsp;<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&apos;</code>)</li>
    <li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
    <li>All your functions and coroutines must be type-annotated.</li>
</ul>
<h2>Install Redis on Ubuntu 18.04</h2>
<pre><code>$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i &quot;s/bind .*/bind 127.0.0.1/g&quot; /etc/redis/redis.conf
</code></pre>
<h2>Use Redis in a container</h2>
<p>Redis server is stopped by default - when you are starting a container, you should start it with:&nbsp;<code>service redis-server start</code></p>