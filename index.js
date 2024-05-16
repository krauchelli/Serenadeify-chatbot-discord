// Require the necessary discord.js classes
const { Client, Events, GatewayIntentBits, IntentsBitField } = require('discord.js');
const dotenv = require('dotenv');

//running dotenv
dotenv.config();
const token = process.env.DISCORD_BOT_TOKEN;
// Create a new client instance
const client = new Client({ 
    intents: [
        GatewayIntentBits.Guilds,
        IntentsBitField.Flags.GuildMembers,
        IntentsBitField.Flags.GuildMessages,
        IntentsBitField.Flags.MessageContent
    ] 
});

// When the client is ready, run this code (only once).
// The distinction between `client: Client<boolean>` and `readyClient: Client<true>` is important for TypeScript developers.
// It makes some properties non-nullable.
client.once(Events.ClientReady, readyClient => {
	console.log(`Ready! Logged in as ${readyClient.user.tag}`);
});

//test slash command
client.on('messageCreate', async message => {
    console.log(message.content);
    if (message.content === 'ping') {
        message.channel.send('Pong.');
    }
    else if (message.content === 'Pong.') {
       message.channel.send('ping'); 
    }
});

// Log in to Discord with your client's token
client.login(token);
