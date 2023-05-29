<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/12/817248fb77fb5c2cef3f.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230529%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230529T210933Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0b158d783f1ab829d52f8014a814ff359f061484ea1a88c57290e8aedb0ffb12" alt=""></p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
    <li><a href="https://intranet.hbtn.io/rltoken/AJdJxuoO8o3hwpybQaFSDQ" title="Classes" target="_blank">Classes</a></li>
    <li><a href="https://intranet.hbtn.io/rltoken/jF42Fw5HNIPnFWKmDzVg1g" title="Metaprogramming" target="_blank">Metaprogramming</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.hbtn.io/rltoken/njFFGENoXPXVPrxCyuHqMg" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<ul>
    <li>How to define a Class</li>
    <li>How to add methods to a class</li>
    <li>Why and how to add a static method to a class</li>
    <li>How to extend a class from another</li>
    <li>Metaprogramming and symbols</li>
</ul>
<h2>Requirements</h2>
<ul>
    <li>All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x</li>
    <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code>,&nbsp;<code>Visual Studio Code</code></li>
    <li>All your files should end with a new line</li>
    <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
    <li>Your code should use the&nbsp;<code>js</code> extension</li>
    <li>Your code will be tested using&nbsp;<code>Jest</code> and the command&nbsp;<code>npm run test</code></li>
    <li>Your code will be verified against lint using ESLint</li>
    <li>Your code needs to pass all the tests and lint. You can verify the entire project running&nbsp;<code>npm run full-test</code></li>
</ul>
<h2>Setup</h2>
<h3>Install NodeJS 12.11.x</h3>
<p>(in your home directory):</p>
<pre><code>curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
</code></pre>
<pre><code>$ nodejs -v
v12.11.1
$ npm -v
6.11.3
</code></pre>
<h3>Install Jest, Babel, and ESLint</h3>
<p>in your project directory:</p>
<ul>
    <li>Install Jest using:&nbsp;<code>npm install --save-dev jest</code></li>
    <li>Install Babel using:&nbsp;<code>npm install --save-dev babel-jest @babel/core @babel/preset-env</code></li>
    <li>Install ESLint using:&nbsp;<code>npm install --save-dev eslint</code></li>
</ul>