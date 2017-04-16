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

If you would like to test our program with a new text file of tweets for any state, you can change the first parameter in the trump_and_hillary_tweets_for_state function on line 122 in get_tweets.py to include your choice of state initials and generate a new batch of tweets for that state. Then, run the file as follows in order to generate a new file of tweets for your chosen state:
```bash
python get_tweets.py
```

## Program Files:
### conservative.txt, liberal.txt
These files contain 100 conservative and 100 liberal manually labeled tweets used to train our system. The tweets were selected from September 6th, 2016 to October 10th, 2016.

### get_tweets.py

### process_tweets.py

### train.py
 
### friendship.py, get_follower_id.py
