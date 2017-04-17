# 486 Project: Analyzation of Users' Support for Political Parties in a State Based on Twitter Data

Group Members:
* Chitra Ramanathan (ramanac)
* Samuel Han (samthan)
* Xiaofan Tan (xiaofant)
* Yawen Luo (yawenluo)

## Project Setup/Installations:
Below are all of the necessary modules that are required to run our program.

### For Getting Tweets:
```bash
pip install pandas
pip install python-twitter
```

### For processing tweets:
```bash
pip install tweet-preprocessor
```

### For functions in friendship.py:
```bash
pip install tweepy
```

## Running the Program:
To run the program using our previously generated text files containing tweets from different states:
* For one single state's election results:
```bash
python 486project.py <STATE INITIALS>
```
Example for collecting California's election results:
```bash
python 486project.py CA
```
* For all state's election results and overall system accuracy:
```bash
python 486project.py ALL
```

If you would like to test our program with a new text file of tweets for any state, you can run get_tweets.py with the state initials as a command line argument.
```bash
python get_tweets.py <STATE INITIALS>
```

This will generate a new file of tweets for your chosen state.

Example for generating a new set of testing tweets for MI:
```bash
python get_tweets.py MI
```

## Program Files:
### conservative.txt, liberal.txt
These files contain 100 conservative and 100 liberal manually labeled tweets used to train our system. The tweets were selected from September 6th, 2016 to October 10th, 2016.

### get_tweets.py
In order to gather all of the tweets to test our model for different states, get_tweets.py includes functions used to gather 100 tweets from each of 50 random cities.

### process_tweets.py
This file contains the functions necessary to pre-process the tweets before they are utilized to train and test our system.

### train.py
This file contains the functions necessary to train/test the Naive Bayes model utilized in our system. In addition, the testNaiveBayes function is modified such that in addition to calculating the Naive Bayes classification, it also considers the presence of popular political hashtags in its calculations. Parts of the testNaiveBayes function are commented out as we tried implementing a metric that would determine whether a user followed popular liberal or conservative users; however, we ran into issues with Twitter's rate-limiting API.

Lastly, this file includes a function used to compare the results of our model to the 2016 Presidential Election results, and calculate our model's accuracy.
 
### friendship.py, get_follower_id.py
These files were used to create the followers metric briefly mentioned in train.py; this metric would allow us to see if users were following well-known conservative or liberal users. Although we were not able to use this metric due to API restrictions, we tried to implement these functions in a few different ways and kept the files in case we decide to re-visit this metric in the future. 

### 486project.py
This file contains the main() of our project. It handles different command line arguments (as mentioned above in 'Running the Program') to test our system.

## Datasets
### Annotated Data (Training Data)
- conservative.txt
- liberal.txt
### Raw Data for each state
Files in dataset/ are raw data for tweets collected in each state. Filenames are following the format of tweets_[state].txt
