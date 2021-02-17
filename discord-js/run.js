// import discord.js package
// npm install discord.js
const discord = require('discord.js');

// Creating client object
const myClient = new discord.Client()

// A message is an event, and when it happens, we want our bot to respond to that message 
// on is an event listener, so on message, we want to check the content of the messagem if it is "hello ", send back "hello my friend".
myClient.on("message", message => {
  if (message.content === "hello") {
    message.channel.send("Hello my friend!")
  }
  if (message.content === "hi") {
    message.channel.send("Howdy 👋 !")
  }
  if (message.content === "Привет") {
    message.channel.send("Привет мои друг!")
  }
});

// Login through token (permission)
myClient.login('your token goes here')
