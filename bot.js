

const { REST } = require('@discordjs/rest');
const { Routes } = require('discord-api-types/v9');

const readline = require('readline');


const commands = [{
  name: 'goodmorning',
  description: 'Sends a good morning message!',
  },
  {
  name: 'ping',
  description: 'ping pong',
  }];

const rest = new REST({ version: '9' }).setToken('TOKEN');

(async () => {
  try {
    console.log('Started refreshing application (/) commands.');

    await rest.put(
      Routes.applicationGuildCommands('657102106007961620', '798767830823600128'),
      { body: commands },
    );

    console.log('Successfully reloaded application (/) commands.');
  } catch (error) {
    console.error(error);
  }
})();

const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages] });

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}`);
  console.log(`WebSocket Ping: ${client.ws.ping}ms`);
});

client.on('interactionCreate', async (interaction) => {
  if (!interaction.isCommand()) return;

  const { commandName } = interaction;

  if (commandName === 'goodmorning') {
    await interaction.reply('Good morning!');
  }

  if (commandName === 'ping') {
    console.log('pong ' + client.ws.ping);

    await interaction.reply('pong ' + client.ws.ping); // client.ws.ping gives the bot's latency
  }

  
});

client.login('token');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Bot is running. Type "STOP" to quit: ', (answer) => {
  if (answer.toUpperCase() === 'STOP') {
    console.log('Stopping the bot...');
    client.destroy();
    rl.close();
    process.exit(0);
  } else {
    console.log(`Invalid command: ${answer}`);
    rl.close();
  }
});