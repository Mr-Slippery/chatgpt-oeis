# On-Line Encyclopedia of Integer Sequences plugin for ChatGPT

A plugin that queries the OEIS in case the user input looks like an integer sequence.
It is based on the plugins-quickstart repo.

If you do not already have plugin developer access, please [join the waitlist](https://openai.com/waitlist/plugins).

## Setup

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin, enter the following command:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! You can start with a message like "0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23". ChatGPT should delegate this to the OEIS Plugin and you should see a response like:

```
The sequence you provided is known as Recamán's sequence. Here's how it's generated:

Start with a(0) = 0.
For each subsequent n > 0, calculate a(n) as follows:
If a(n-1) - n is positive and not already in the sequence, then a(n) = a(n-1) - n.
Otherwise, a(n) = a(n-1) + n.
```

## Getting help

If you run into issues or have questions building a plugin, please join our [Developer community forum](https://community.openai.com/c/chat-plugins/20).
