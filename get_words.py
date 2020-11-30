import pickle


with open('words.txt','r') as f:

    lines = f.readlines()


lines = [line.strip() for line in lines if len(line) >= 3]


pickle.dump(lines,open('words.pkl','wb'))





