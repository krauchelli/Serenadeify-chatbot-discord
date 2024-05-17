const client = require('../index');

const analyzeSentiment = async (sentence) => {
    return sentence;
}

// Function to handle incoming messages
const handleMessage = async (message) => {
    if(message.author.bot) return;

    // Check if the message contains 'ping'
    if (message.content.includes('ping')) {
        message.channel.send('Pong! ');
    }

    // Check if the message contains 'hi serena' and not inside a thread
    if (message.content.includes('hi serena') && !message.channel.isThread()) {
        const messageAuthor = message.author.username;
        const replyMessage = await message.reply(`hi! ${messageAuthor}, how are you doing?`); // base message

        replyMessage.startThread({ // Start the thread after the reply is sent
            name: `Song Recommendation to: ${messageAuthor}-${message.createdTimestamp}`,
            autoArchiveDuration: 60,
            type: 'GUILD_PUBLIC_THREAD'
        });        
    } 
    
    // Check if the message contains 'i feel like' and inside a thread
    if (message.content.includes('i feel like') && message.channel.isThread()) {
        const messageAuthor = message.author.username;
        const sentimentText = message.content.slice('i feel like'.length).trim();
        const sentenceJson = JSON.stringify(sentimentText);
        console.log(sentenceJson);
        message.reply(`I see!`);
    }
    console.log(message.content);
};

module.exports = {
  handleMessage,
};
