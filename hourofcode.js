#! /usr/bin/nodejs
var stdio = require('stdio');
var name="world";

var ops = stdio.getopt({
  "name":{key:"n", args:1, description:"who am I saying hello to?"}
});
if(ops.name){
  name = ops.name;
}
console.log("Hello "+name);
