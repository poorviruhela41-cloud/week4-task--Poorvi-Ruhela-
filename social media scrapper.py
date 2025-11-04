import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string

# Download NLTK stopwords (only first time)
nltk.download('stopwords')

class NewsScraperAnalyzer:
    def __init__(self, url="https://www.bbc.com/news"):
        self.url = url
        self.headlines = []

    def scrape_headlines(self):
        """Scrape latest news headlines."""
        print(f"Scraping data from {self.url} ...")
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all headlines (BBC style)
        items = soup.find_all('h2')
        for tag in items:
            text = tag.get_text(strip=True)
            if len(text) > 15:  # filter very short titles
                self.headlines.append(text)

        print(f"✅ Found {len(self.headlines)} headlines.")
        return self.headlines

    def save_to_csv(self, filename="headlines.csv"):
        """Save headlines to CSV."""
        df = pd.DataFrame(self.headlines, columns=["Headline"])
        df.to_csv(filename, index=False)
        print(f"💾 Headlines saved to {filename}")

    def clean_text(self, text):
        """Remove punctuation, lowercase, and stopwords."""
        stop_words = set(stopwords.words('english'))
        translator = str.maketrans('', '', string.punctuation)
        words = text.lower().translate(translator).split()
        filtered = [w for w in words if w not in stop_words and len(w) > 2]
        return filtered

    def analyze_text(self):
        """Perform text analysis."""
        if not self.headlines:
            print("No data found. Please scrape first.")
            return

        all_words = []
        for headline in self.headlines:
            all_words.extend(self.clean_text(headline))

        # Most common words
        word_freq = Counter(all_words)
        print("\n🔤 Top 10 Most Common Words:")
        for word, freq in word_freq.most_common(10):
            print(f"{word}: {freq}")

        # Longest headline
        longest = max(self.headlines, key=len)
        print("\n📰 Longest Headline:")
        print(longest)

        # Word cloud visualization
        self.generate_wordcloud(word_freq)

    def generate_wordcloud(self, word_freq):
        """Generate word cloud."""
        if not word_freq:
            print("No words to generate word cloud.")
            return

        print("\n☁️ Generating word cloud...")
        wc = WordCloud(width=800, height=400, background_color="white")
        wc.generate_from_frequencies(word_freq)
        plt.figure(figsize=(10,5))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.title("Word Cloud of News Headlines")
        plt.show()


def main():
    scraper = NewsScraperAnalyzer("https://www.bbc.com/news")
    scraper.scrape_headlines()
    scraper.save_to_csv()
    scraper.analyze_text()

if __name__ == "__main__":
    main()