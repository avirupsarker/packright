// api.js
class API {
    static async callGemini(systemInstruction, userPrompt) {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ systemInstruction, userPrompt })
        });

        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.error || 'Failed to fetch from server');
        }

        const data = await response.json();
        const content = data.candidates[0].content.parts[0].text;
        return JSON.parse(content);
    }

    static async extractTripContext(promptText) {
        const systemInstruction = `You are a deterministic trip extraction engine. Read the user's travel prompt and extract the requested details into a strict JSON object. Do not guess or invent data. If something is unknown, omit it or set it to null.

Strict JSON format required:
{
  "rawDescription": "string",
  "destination": "string or null",
  "normalizedDestination": "string or null",
  "country": "string or null",
  "region": "string or null",
  "travelMonth": "string or null",
  "durationDays": "number or null",
  "travelerCount": "number or null",
  "travelerTypes": ["adult", "child", "infant", "senior"],
  "activities": ["string"],
  "skillLevel": "beginner|intermediate|advanced|null",
  "accommodationType": "string or null",
  "rentalItems": ["string"],
  "ownedItems": ["string"],
  "luggageConstraints": "string or null",
  "weatherProfile": ["string"]
}

Normalize synonyms (e.g., ski/skiing, snowboard/snowboarding). 
Always preserve the original text in rawDescription.`;

        return this.callGemini(systemInstruction, promptText);
    }

    static async getClarifierQuestions(promptText) {
        const systemInstruction = `You are an intelligent travel packing assistant. Based on the user's travel prompt, generate 2-3 multiple-choice clarifying questions to better understand their needs and remove template ambiguity.
Strict JSON format required:
{
  "questions": [
    {
      "id": "q1",
      "question_text": "What type of accommodation are you staying in?",
      "options": ["Hotel / Airbnb", "Backpacker Hostel", "Camping / Outdoors"]
    }
  ]
}`;
        return this.callGemini(systemInstruction, promptText);
    }

    static async getPackingChecklist(tripContext, answers) {
        const systemInstruction = `You are an expert travel packing consultant. Read the structured TripContext and generate a highly personalized, practical checklist.

## INSTRUCTIONS
- Categorize items (e.g., Clothing, Electronics, Toiletries).
- Output items with a status: 'needed', 'owned', 'rent', or 'optional'.
- If the user explicitly stated they own an item, mark it 'owned'.
- If they stated they are renting an item (like skis), mark it 'rent'.
- Include a brief 'includedBecause' or 'omittedBecause' reasoning for non-obvious items.
- Respect duration: adjust quantities correctly.
- Add activity-specific, weather-specific, and destination-specific items.
- NEVER append affiliate product links, ASINs, or prices.

## OUTPUT FORMAT
Respond ONLY with valid JSON matching this exact structure:
{
  "trip_summary": "Short trip summary, e.g., '7 days in Niseko in January · skiing · renting skis'",
  "categories": [
    {
      "name": "Category name",
      "items": [
        {
          "name": "Item name, clean and short",
          "quantity": "2x (or omit if 1)",
          "requiredLevel": "essential", // 'essential', 'recommended', 'optional'
          "status": "needed", // 'needed', 'owned', 'rent', 'optional'
          "includedBecause": ["reason 1"]
        }
      ]
    }
  ]
}`;
        
        let promptBody = `TripContext: ${JSON.stringify(tripContext, null, 2)}`;
        if (answers && answers.length > 0) {
            promptBody += `\n\nClarifying Answers:\n${answers.map(a => `- ${a.question}: ${a.answer}`).join('\n')}`;
        }
        return this.callGemini(systemInstruction, promptBody);
    }
}
