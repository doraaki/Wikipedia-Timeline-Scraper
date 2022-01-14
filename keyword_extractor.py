import pathlib
from page_parser import parse_video_game_page
import pke

def extract_keywords(event_text):
    # initialize keyphrase extraction model, here TopicRank
    extractor = pke.unsupervised.TopicRank()

    # load the content of the document, here document is expected to be in raw
    # format (i.e. a simple text file) and preprocessing is carried out using spacy
    extractor.load_document(input=event_text, language='en')

    # keyphrase candidate selection, in the case of TopicRank: sequences of nouns
    # and adjectives (i.e. `(Noun|Adj)*`)
    extractor.candidate_selection()

    # candidate weighting, in the case of TopicRank: using a random walk algorithm
    extractor.candidate_weighting()

    # N-best selection, keyphrases contains the 10 highest scored candidates as
    # (keyphrase, score) tuples
    keyphrases = extractor.get_n_best(n=10)
    
    return keyphrases


def main():
    path = pathlib.Path(__file__).resolve().parent.joinpath('topics', 'video-games', '2021.txt').__str__()
    file = open(path, 'r')
    events = parse_video_game_page(list(file.readlines()))
    print(events)
    for event in events:
        print(extract_keywords(event['EVENT']))

if __name__ == '__main__':
    main()