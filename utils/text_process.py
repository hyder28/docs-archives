from utils.constants import keywords_lookup
import collections

import logging


def get_topic_keywords(text_content):
    try:
        text_content = text_content.lower()

        tagged_keywords = []

        for label_class, keyword_list in keywords_lookup.items():
            for keyword in keyword_list:
                keyword = keyword.lower()

                if keyword in text_content:
                    tagged_keywords.append(label_class)

        ctr = dict(collections.Counter(tagged_keywords).most_common(3))

        return {"ARTICLE_TOPIC": str(ctr), "ARTICLE_TEXT": text_content}

    except Exception as e:
        logging.error(f"> error in text topic extraction by keywords: {e}")
        return {}
