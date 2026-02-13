import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
# In‑memory store for test cases and results
session_testcases = {}
session_results = {}


@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I am your MIT Assignment Bot.")

@bot.command()
async def testcases(ctx, *, prompt):
    # Simple placeholder logic for assignment
    await ctx.send(f"Generating test cases for: {prompt}\n1. Input validation\n2. Edge case handling\n3. Error response behavior")


@bot.command()
async def fraudhallucination(ctx, *, model_output):
    """
    Evaluates a fraud-related model output for hallucination risk.
    """
    red_flags = [
        "guaranteed fraud",
        "100% certain",
        "blacklisted everywhere",
        "all transactions are fraudulent",
        "customer is always a mule"
    ]

    flagged_phrases = [p for p in red_flags if p.lower() in model_output.lower()]

    if flagged_phrases:
        risk = "HIGH"
        reason = "Overconfident or absolute language detected in fraud classification."
    else:
        risk = "MODERATE"
        reason = "No obvious overclaims, but fraud decisions should always be probabilistic."

    response = (
        "🧠 **Fraud Hallucination Check**\n\n"
        f"**Model Output:** {model_output}\n"
        f"**Hallucination Risk:** {risk}\n"
        f"**Reason:** {reason}\n"
        "🔎 Recommendation: Ensure fraud models use scores/probabilities, not absolute statements."
    )

    await ctx.send(response)

@bot.command()
async def fraudcompliance(ctx, *, text):
    """
    Evaluates fraud investigation text for PII and policy risks.
    """
    pii_indicators = ["ssn", "social security", "passport", "driver's license", "dob", "date of birth"]
    sensitive_terms = ["blacklist", "de-risk this customer", "block all activity", "suspicious ethnicity"]

    pii_hits = [p for p in pii_indicators if p.lower() in text.lower()]
    sensitive_hits = [s for s in sensitive_terms if s.lower() in text.lower()]

    response = "⚖️ **Fraud Compliance Review**\n\n"
    if pii_hits:
        response += f"🔴 **PII Indicators Detected:** {', '.join(pii_hits)}\n"
    else:
        response += "🟢 No obvious PII indicators detected.\n"

    if sensitive_hits:
        response += f"🔴 **Sensitive / Policy-Risky Phrases Detected:** {', '.join(sensitive_hits)}\n"
    else:
        response += "🟢 No obvious policy-risky language detected.\n"

    response += (
        "\n📌 Recommendation: Ensure fraud notes avoid unnecessary PII exposure and discriminatory language. "
        "Use neutral, risk-based terminology."
    )

    await ctx.send(response)

@bot.command()
async def fraudrisk(ctx, *, scenario):
    """
    Simulates a fraud risk score based on scenario keywords.
    """
    high_risk_keywords = ["new device", "foreign country", "high value", "vpn", "tor", "password reset", "mule"]
    medium_risk_keywords = ["unusual pattern", "new merchant", "multiple attempts", "failed login"]

    score = 10  # base
    explanation = []

    lower_scenario = scenario.lower()

    if any(k in lower_scenario for k in high_risk_keywords):
        score += 60
        explanation.append("High-risk indicators detected (device/geo/value/ATO/mule patterns).")

    if any(k in lower_scenario for k in medium_risk_keywords):
        score += 20
        explanation.append("Medium-risk behavioral or merchant indicators detected.")

    if score < 30:
        level = "LOW"
    elif score < 60:
        level = "MEDIUM"
    else:
        level = "HIGH"

    response = (
        "📈 **Simulated Fraud Risk Scoring**\n\n"
        f"**Scenario:** {scenario}\n"
        f"**Risk Score:** {score} / 100\n"
        f"**Risk Level:** {level}\n"
        f"**Explanation:** {' '.join(explanation) if explanation else 'No strong fraud indicators detected.'}\n"
        "📌 Note: This is a simulated scoring model for demonstration, not a production risk engine."
    )

    await ctx.send(response)


# ---------------------------------------------------------
# 1. Generate Test Cases
# ---------------------------------------------------------

@bot.command()
async def design(ctx, *, scenario):
    """
    Generates fraud‑specific test cases aligned with banking fraud detection workflows.
    """
    fraud_testcases = [
        {
            "id": 1,
            "type": "Velocity Check",
            "description": f"Simulate rapid consecutive transactions for: {scenario}",
            "expected": "System should flag abnormal transaction frequency."
        },
        {
            "id": 2,
            "type": "Geolocation Mismatch",
            "description": f"Test login from unusual country followed by high‑value transfer for: {scenario}",
            "expected": "System should trigger step‑up authentication."
        },
        {
            "id": 3,
            "type": "Device Fingerprint",
            "description": f"Attempt transaction from new device not seen in customer profile for: {scenario}",
            "expected": "System should require OTP or block transaction."
        },
        {
            "id": 4,
            "type": "Mule Account Pattern",
            "description": f"Simulate small deposits followed by immediate withdrawals for: {scenario}",
            "expected": "System should classify account as high‑risk."
        },
        {
            "id": 5,
            "type": "Behavioral Anomaly",
            "description": f"Customer suddenly performs unusual high‑value transfer for: {scenario}",
            "expected": "System should assign high anomaly score."
        },
        {
            "id": 6,
            "type": "Compromised Credentials",
            "description": f"Simulate login from TOR/VPN for: {scenario}",
            "expected": "System should block or challenge login."
        },
        {
            "id": 7,
            "type": "Merchant Risk",
            "description": f"Transaction routed to known fraudulent merchant category for: {scenario}",
            "expected": "System should decline or escalate."
        },
        {
            "id": 8,
            "type": "Account Takeover",
            "description": f"Password reset followed by immediate transfer for: {scenario}",
            "expected": "System should trigger ATO workflow."
        }
    ]

    session_testcases[ctx.author.id] = fraud_testcases

    response = f"🛡️ **Fraud Test Cases Generated for:** `{scenario}`\n\n"
    for tc in fraud_testcases:
        response += (
            f"**TC{tc['id']} – {tc['type']}**\n"
            f"• Scenario: {tc['description']}\n"
            f"• Expected Behavior: {tc['expected']}\n\n"
        )

    await ctx.send(response)


# ---------------------------------------------------------
# 2. Execute Test Cases (Simulated)
# ---------------------------------------------------------
@bot.command()
async def execute(ctx):
    """
    Executes fraud test cases with realistic fraud detection outcomes.
    """
    user_id = ctx.author.id

    if user_id not in session_testcases:
        await ctx.send("⚠️ No fraud test cases found. Please run `!design <scenario>` first.")
        return

    testcases = session_testcases[user_id]
    results = []

    for tc in testcases:
        # Fraud detection systems often fail edge cases → weighted randomness
        outcome = random.choices(
            ["PASS", "FAIL"],
            weights=[0.7, 0.3],  # 70% pass, 30% fail
            k=1
        )[0]

        results.append({
            "id": tc["id"],
            "type": tc["type"],
            "scenario": tc["description"],
            "expected": tc["expected"],
            "result": outcome
        })

    session_results[user_id] = results

    response = "🚨 **Executing Fraud Detection Test Cases...**\n\n"
    for r in results:
        emoji = "🟢" if r["result"] == "PASS" else "🔴"
        response += f"{emoji} **TC{r['id']} – {r['type']}** → {r['result']}\n"

    await ctx.send(response)
  

# ---------------------------------------------------------
# 3. QA Report
# ---------------------------------------------------------
@bot.command()
async def report(ctx):
    """
    Generates a fraud‑specific QA report summarizing detection performance.
    """
    user_id = ctx.author.id

    if user_id not in session_results:
        await ctx.send("⚠️ No executed results found. Please run `!execute` first.")
        return

    results = session_results[user_id]
    passed = sum(1 for r in results if r["result"] == "PASS")
    failed = sum(1 for r in results if r["result"] == "FAIL")

    response = (
        "📊 **Fraud Detection QA Report**\n\n"
        f"**Total Test Cases:** {len(results)}\n"
        f"**Passed:** {passed}\n"
        f"**Failed:** {failed}\n\n"
        "📝 **Detailed Results:**\n"
    )

    for r in results:
        emoji = "🟢" if r["result"] == "PASS" else "🔴"
        response += (
            f"{emoji} TC{r['id']} – {r['type']}\n"
            f"• Scenario: {r['scenario']}\n"
            f"• Expected: {r['expected']}\n"
            f"• Result: {r['result']}\n\n"
        )

    await ctx.send(response)


# ---------------------------------------------------------
# 4. Reset Session (Optional)
# ---------------------------------------------------------
@bot.command()
async def reset(ctx):
    """
    Clears stored test cases and results for the user.
    """
    user_id = ctx.author.id
    session_testcases.pop(user_id, None)
    session_results.pop(user_id, None)

    await ctx.send("🔄 Your test session has been reset.")

# ---------------------------------------------------------
# Run the Bot
# ---------------------------------------------------------

bot.run("BOT CODE")
