# Twitter Sentiment Analysis

Repository with all the files/scripts I used for Twitter sentiment analysis on gun related tweets. Project was for the MISA 2018 Coding Challenge (Case Competition)

Synopsis:
Goal was to investigate interesting causes of gun violence in America. I decided to analyze the sentiment towards guns across U.S. states. To gather data, I turned to the Twitter platform as it is a decent representation of sentiment. Used Scikit-learn and NLTK to process Twitter tweets retrieved using Twitter's API (Tweepy). Was able to identify a slight correlation between gun ownership rate per person and sentiment towards guns.

Technologies used: Python, machine learning, natural language processing, Tableau, Git

## Walkthrough

1. Generate the classifiers based on the Twitter dataset (generate_classifiers.py).

    a. Downloaded Ibrahim Naji's Twitter Sentiment Analysis Training Corpus to train with (Only used 10,000 tweets).
    b. Read in the Twitter dataset
    c. Used NLTK's word_tokenize function to tokenize the words in the tweet.
    d. Get the features set of the Twitter dataset (top 3000 words that appear) and parse each tweet leaving only words that appear in the feature set.
    e. Train the classifiers using the feature set. Ran NLTK's Naive Bayes algorithm and Scikit-learn's Multinomial NB, Bernoulli NB, Linear SVC, Nu SVC, and Logistic Regression.
    f. Pickle dataset used and classiers. (Pi)
    
    *Screenshot of the Twitter dataset used to train classifiers*
    <img src='Screenshots/twitter_dataset_screenshot' title='Screenshot of twitter dataset' width='' alt='Screenshot of dataset' />

2. Test the classifier with the gun dataset (test_gun_dataset.py).

    a. Read in the Twitter gun related dataset which we will test the classifiers on (retrieved using DiscoverText and Sifter).
    b. Create a feature set and then a testing set (same as what we did previously in step 1).
    c. Run the NLTK.classify.accuracy function.
    
    *Screenshot of the classifiers accuracy*
    <img src='Screenshots/test_classifiers_screenshot' title='Screenshot of test classifiers' width='' alt='Screenshot of test classifiers' />
    
    Notes:
    - The Twitter gun related dataset was historical data retrieved in February (we retrieved historical data at first because Tweepy for was not letting us stream tweets. However, I will address this in my conclusion)
    - Accuracy was averaging about 60 percent if we remove the LogisticRegression and NLTK's NB.
    - I tested the classifiers on the dataset I trained them in, and it produced around a 77 percent accuracy. So a noticeable drop.
    - To investigate bias, I tested the training set on exclusively positive and then negative tweets. The result was a noticeable negative bias towards tweets.
    
3. Stream Twitter data and record the sentiment value using the sentiment_analysis_module.py (twitter_stream.py).

    a. Set up a Twitter app and set our access token using Oath to connect to the Twitter API
    b. Stream tweets related the 'guns' and write them into a csv file.
    c. Write in location, text, and sentiment polarity. Sentiment polarity is the net of the probability of positive and negative sentiment. (ex. A sentiment polarity of '1' would mean the tweet is 100 percent chance of being positive and 0 percent change of being negative)
    d. Collect in about 22,000 tweets
    
    *Screenshot of the Twitter tweets collected*
    <img src='Screenshots/twitter_stream_screenshot' title='Screenshot of Twitter stream' width='' alt='Screenshot of Twitter stream' />
    
     Notes:
     - Some of the tweets do not have a location. This will be addressed in the next step.
    
4. Parse the Twitter stream data for only tweets with location (parse_twitter_stream.py)

    a. Parse the Twitter stream data for tweets with locations. The sentiment analysis is to group tweet sentiment by state.
    b. Search for key words such as "Texas" or "TX" and write the filtered Twitter stream data into another csv.
    
    *Screenshot of the parsed Twitter tweets collected*
    <img src='Screenshots/twitter_stream_parsed_screenshot' title='Screenshot of Twitter stream' width='' alt='Screenshot of Twitter stream' />
    
5. Sort the parsed Twitter data by state (sort_twitter_stream_data.py)

    a. Group the data by state and calculate average sentiment polarity.
    b. Visualize result on Tableau.

    *Visualization of the result (via Tableau)*
    <img src='Screenshots/tableau_visual_screenshot' title='Screenshot of Tableau' width='' alt='Screenshot of Tableau' />

6. Analysis

    If you look at the midwest and southeast United States, you can see there is a slightly more negative sentiment compared to the other states.
    <img src='Screenshots/tableau_visual_analysis_screenshot' title='Screenshot of Tableau analysis' width='' alt='Screenshot of tableau analysis' />
    
    And if we look at the gun ownership rate per person, there is some correlation.
    <img src='Screenshots/gun_ownership_screenshot' title='Screenshot of gun ownership' width='' alt='Screenshot of gun ownership' />

    So the more negative sentiment a person is towards guns, the higher the gun ownership rate. It is an almost opposite type of result I was expecting.

    (Please note that the methods I used most likely generated random errors. I have not been scrutinized on my project and as a result everything should be taken with a grain of salt. )
    
7. Conclusion

    Overall, I learned a lot during this project. I strengthened my Python scripting skills and exposed myself to powerful libraries like NLTK and Scikit-learn. In addition, I utilized Twitter's API in a unique way to investigate a controversial problem in the United States.
    
    Some things in the future to improve this data analysis project:
    - [ ] Train with data is more gun related. Couldn't do this as I did not have the time to label 10,000+ Twitter tweets.
    - [ ] Addressing a note I made in step 2, used Twitter stream data to test accuracy.
    - [ ] Explore different machine learning algorithms.
    - [ ] Train with a larger dataset. Training with 10,000 Tweets already gave my Mac Air a hard time, so I would like a more computationally powerful computer.
    - [ ] I only used the BNB and MNB classifiers to classify tweets as I could not figure out how to extract probability from the Linear SVC and Nu SVC classifiers.
    - [ ] Twitter data is dirty. Perhaps a different approach?
    
    Again, this was my first data analysis project, and I am still learning. If you have any suggestions or possible errors I made, I urge you to message me, so I can investigate further.

## Libraries / Datasets Used
*Libraries*
- [x] Natural Language Toolkit (NLTK)
- [x] Twitter API (Tweepy)
- [x] Machine Learning (scikit-learn)
- [x] CSV
*Datasets*
- [x] Twitter Sentiment Analysis Training Corpus by Ibrahim Naji (http://thinknook.com/twitter-sentiment-analysis-training-corpus-dataset-2012-09-22/)
- [x] Gun Ownership Statistics (http://demographicdata.org/facts-and-figures/gun-ownership-statistics/ )

## Notes
- The Twitter dataset by Ibrahim Naji that I used is removed as it is too big to upload to GitHub. However, there is a pickled dataset with the tweets I used.
- Cleaned up code and file directories. Unsure if program will function how it intends to.

## License

Copyright [2018] [Henry Vuong]

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

