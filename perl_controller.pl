#!/usr/bin/perl

#Here we go, hacking it all together in perl.
#We'll be using python's nltk module to make a syntax table of the original sentences.

system("python POS_tagger.py < Tjagonaj_test_cases.txt > rearranged_test_cases.txt");

system("snobol4 Tjagonaj_translator_w_dictionary.sno < rearranged_test_cases.txt > Tjagonaj_translated.txt");
