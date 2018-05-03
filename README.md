# Twitter Sentiment Analysis

Repository with all the files/scripts I used for Twitter sentiment analysis on guns. Project was for the MISA 2018 Coding Challenge (Case Competition)

## Walkthrough (will add gifs later)

1. Generate the classifiers based on the Twitter dataset (generate_classifiers.py).
2. Test the classifier with the gun dataset (test_gun_dataset.py).
3. Stream Twitter data and record the sentiment value using the sentiment_analysis_module.py (twitter_stream.py).
4. Parse the Twitter stream data for only tweets with location (parse_twitter_stream.py)
5. Sort the parsed Twitter data by state (sort_twitter_stream_data.py)
6. Profit.

Here is the visualization of the result (via Tableau):

<img src='https://i.imgur.com/gYL7IgM.png' title='Screenshot of Tableau' width='' alt='Screenshot' />


## Libraries / Datasets Used

**Libraries**
- [x] Natural Language Toolkit (NLTK)
- [x] Twitter API (Tweepy)
- [x] Machine Learning (scikit-learn)

**Datasets**
- [x] Twitter Sentiment Analysis Training Corpus by Ibrahim Naji (http://thinknook.com/twitter-sentiment-analysis-training-corpus-dataset-2012-09-22/)
- [x] Twitter Gun related Datset from historical Twitter data (DiscoveryText/Sifter)

## Notes
- The Twitter dataset by Ibrahim Naji that I used is removed as it is too big to upload to GitHub. However, there is a pickled dataset with the tweets I used
- classifer accuracy about 77 percent for Twitter datset found online
- classifer accuracy about 60 percent for gun dataset
- Linear SVC came out as the most accurate but could not figure out how to extract probability (hence, only MNB and BNB classifier was used)
- cleaned up code and file directories. Unsure if program will function how it intends to

## License

Copyright [2018] [Henry Vuong]

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
