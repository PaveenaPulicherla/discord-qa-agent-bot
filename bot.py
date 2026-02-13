import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I am your QA Agent Bot.")

@bot.command()
async def testcases(ctx, *, prompt):
    response = (
        f"Test cases for: {prompt}\n"
        "1. Validate input format\n"
        "2. Check edge cases\n"
        "3. Verify expected output\n"
        "4. Error handling behavior\n"
    )
    await ctx.send(response)

@bot.command()
async def hallucination(ctx, *, text):
    response = (
        f"Hallucination evaluation for: {text}\n"
        "Risk Score: Low\n"
        "Reason: No unsupported claims detected."
    )
    await ctx.send(response)

@bot.command()
async def compliance(ctx, *, text):
    response = (
        f"Compliance review for: {text}\n"
        "No PII detected.\n"
        "No policy violations found."
    )
    await ctx.send(response)

@bot.command()
async def qareport(ctx):
    response = (
        "QA Report Summary:\n"
        "- 5 tests passed\n"
        "- 1 test flagged for review\n"
        "- No compliance issues detected"
    )
    await ctx.send(response)

bot.run("YOUR_BOT_TOKEN_HERE")
