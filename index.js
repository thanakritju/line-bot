import { ClientConfig, Client, middleware, MiddlewareConfig, WebhookEvent, TextMessage, MessageAPIResponseBase } from '@line/bot-sdk';

const clientConfig: ClientConfig = {
  channelAccessToken: process.env.CHANNEL_ACCESS_TOKEN || '',
  channelSecret: process.env.CHANNEL_SECRET,
};

const client = new Client(clientConfig);

const response: TextMessage = {
  type: 'text',
  text: "Hello, There",
};