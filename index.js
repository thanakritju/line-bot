'use strict';

const line = require('@line/bot-sdk');
const express = require('express');
const cron = require('node-cron');

// create LINE SDK config from env variables
const config = {
  channelAccessToken: process.env.CHANNEL_ACCESS_TOKEN,
  channelSecret: process.env.CHANNEL_SECRET,
};

// create LINE SDK client
const client = new line.Client(config);

// create Express app
// about Express itself: https://expressjs.com/
const app = express();

// register a webhook handler with middleware
// about the middleware, please refer to doc
app.post('/callback', line.middleware(config), (req, res) => {
  Promise
    .all(req.body.events.map(handleEvent))
    .then((result) => res.json(result))
    .catch((err) => {
      console.error(err);
      res.status(500).end();
    });
});

// event handler
function handleEvent(event) {
  if (event.type !== 'message' || event.message.type !== 'text') {
    // ignore non-text-message event
    return Promise.resolve(null);
  }

  if (event.message.text.startsWith("schedule")) {
    scheduleMessage(event.source.groupId)
    return client.replyMessage(event.replyToken, { type: 'text', text: "Scheduled a message"});
  }
  return Promise.resolve(null);
}

function scheduleMessage(groupId) {
  cron.schedule('20 18 * * *', () => {
    client.pushMessage(groupId, "You have to call to your bf")
  });
  
  cron.schedule('0 6 * * *', () => {
    client.pushMessage(groupId, "Good morning both")
  });
}

// listen on port
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`listening on ${port}`);
});