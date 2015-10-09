
from django.shortcuts import render_to_response

def home(request):
	file_poem = open('ihc_game/poema.txt').read()
	print file_poem
	trap_word = 'clavo'

	txt_lst = file_poem.split()
	n_txt_lst = []
	for i in txt_lst:
		if i != trap_word:
			n_txt_lst.append(i)

	fixed_poem = ' '.join(n_txt_lst)

	return render_to_response('home.html' , {'poema' : file_poem , 'trap_word':trap_word, 'fixed_poem':fixed_poem});


