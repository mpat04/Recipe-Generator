# Recipe Generator
This is a GUI-based recipe generator.

## The Problem
My roommates and I are constantly having to throw out ingredients that go bad because we don't what we could make with them. This was very wasteful and expensive in the long run.

## How to Use
1) Select the cuisine(s) you want.
2) Select your dietary restrictions.
3) Enter the ingredients you want to use.
4) Click the generate button. 

## API
OpenAI's API was used for this program. It is powered by ChatGPT and uses the Chat Completion feature.

## To Use This on Your Computer
1) Go to https://platform.openai.com/docs/overview and login
2) Go to the "API keys" tab
3) Press the "Create new secret key" and "Create secret key"

For Window:
1) Permanent setup: To make the setup permanent, add the variable through the system properties as follows:
Right-click on 'This PC' or 'My Computer' and select 'Properties'.
Click on 'Advanced system settings'.
Click the 'Environment Variables' button.
In the 'System variables' section, click 'New...' and enter OPENAI_API_KEY as the variable name and your API key as the variable value.
2) Verification: To verify the setup, reopen the command prompt and type the command below. It should display your API key: echo %OPENAI_API_KEY%

For Mac:
1) Open Terminal: You can find it in the Applications folder or search for it using Spotlight (Command + Space).
2) Edit Bash Profile: Use the command nano ~/.bash_profile or nano ~/.zshrc (for newer MacOS versions) to open the profile file in a text editor.
3) Add Environment Variable: In the editor, add the line below, replacing your-api-key-here with your actual API key:
export OPENAI_API_KEY='your-api-key-here'
4) Save and Exit: Press Ctrl+O to write the changes, followed by Ctrl+X to close the editor.
5) Load Your Profile: Use the command source ~/.bash_profile or source ~/.zshrc to load the updated profile.
6) Verification: Verify the setup by typing echo $OPENAI_API_KEY in the terminal. It should display your API key.

Finally run the program!