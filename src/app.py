import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    # api_key="my_api_key",
)
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "As an expert Medium post copywriter, your goal is to create an engaging and potentially viral Medium post from the provided bullet points.\nPlease follow these guidelines to transform the draft into a captivating and shareable piece:\n1. Incorporate humor where appropriate, ensuring relevance and suitability for the content.\n2. Thoughtfully and sparingly use emojis to reinforce the tone and message.\n3. Maintain simplicity, directness, and conciseness, avoiding fluff and complex language.\n4. Write in a universally intelligible English to appeal to global readers.\n5. Follow this post structure:\n- Title: Craft a clickbait title that sparks an emotional reaction from readers.\n- Subheading: Formulate a subheading relevant to the title, making the post more intriguing.\n- Hook: Compose a captivating 1-2 sentence hook that stimulates readers to continue reading.\n- Paragraphs: Ensure paragraphs are brief, engaging, and \nimpactful for readers.\n- Quote: Conclude the post with a relevant, motivational, \nor inspiring quotation associated with the topic.\nInclude headings, subheadings, and lists when applicable, aiming for a visually appealing and easy-to-read format. Your response \nshould exhibit flexibility, accommodating a wide array of \ntopics and drafts while adhering to the essential principles \nof crafting an attention-grabbing Medium post.\nthis article should be introduction level to talk about Anthropic Claude. it has recently announcement of claude 3 which has a better result than chat-gpt4. it is api is free to use which good for a generative ai development while openai require payment to use which is not good for starter to experiment. in this article, talks about what is claude 3? history of anthropic, what is good for anthropic claude 3. what is the use case for anthropic claude 3 api\n"
                }
            ]
        }
    ]
)
print(message.content)