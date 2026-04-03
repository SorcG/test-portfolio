CONTENT_TYPES = [
    "Blog-Artikel",
    "Projektplan",
    "Recherche-Zusammenfassung",
    "E-Mail-Vorlage",
    "Social-Media-Post",
]

_TEMPLATES = {
    "Blog-Artikel": """You are an expert content writer. Write a well-structured blog article about the following topic.

Topic: {topic}

Output the article in Markdown format with this exact structure:
# [Article Title]

## Introduction
[2-3 sentences introducing the topic]

## [Section 1 Title]
[Content for section 1]

## [Section 2 Title]
[Content for section 2]

## [Section 3 Title]
[Content for section 3]

## Conclusion
[2-3 sentences summarizing the key points]

Use bullet points where appropriate.""",

    "Projektplan": """You are a project management expert. Create a structured project plan for the following topic.

Topic: {topic}

Output the plan in Markdown format with this exact structure:
# [Project Title]

## Overview
[2-3 sentences describing the project goal]

## Milestones
- [Milestone 1]
- [Milestone 2]
- [Milestone 3]
- [Milestone 4]

## Tasks
- [Task 1]
- [Task 2]
- [Task 3]
- [Task 4]
- [Task 5]

## Next Steps
- [Immediate action 1]
- [Immediate action 2]
- [Immediate action 3]

Be specific and actionable.""",

    "Recherche-Zusammenfassung": """You are a research analyst. Write a concise research summary about the following topic.

Topic: {topic}

Output the summary in Markdown format with this exact structure:
# [Research Title]

## Key Findings
- [Finding 1]
- [Finding 2]
- [Finding 3]
- [Finding 4]

## Detailed Analysis
[3-4 sentences with deeper analysis]

## Implications
[2-3 sentences about what this means in practice]

## Recommendations
- [Recommendation 1]
- [Recommendation 2]
- [Recommendation 3]

Be factual and concise.""",

    "E-Mail-Vorlage": """You are an expert business writer. Write a professional email about the following topic.

Topic: {topic}

Output the email in Markdown format with this exact structure:
# [Email Subject Line]

## Salutation
[Appropriate greeting]

## Opening
[1-2 sentences stating the purpose of the email]

## Main Content
[3-4 sentences with the core message or request]

## Call to Action
[1 sentence with a clear next step or request]

## Closing
[Professional sign-off]

Keep it concise and to the point.""",

    "Social-Media-Post": """You are a social media expert. Write an engaging LinkedIn post about the following topic.

Topic: {topic}

Output the post in Markdown format with this exact structure:
# [Post Hook - attention-grabbing first line]

## Main Content
[3-5 sentences with the core message, insights or story]

## Key Takeaways
- [Takeaway 1]
- [Takeaway 2]
- [Takeaway 3]

## Call to Action
[1 engaging question or prompt for the audience]

## Hashtags
[5-7 relevant hashtags]

Make it engaging and authentic.""",
}


def get_prompt(topic: str, content_type: str, tone: str, language: str) -> str:
    template = _TEMPLATES[content_type]
    base = template.format(topic=topic)
    return f"{base}\n\nWrite in a {tone.lower()} tone. Respond in {language}."
