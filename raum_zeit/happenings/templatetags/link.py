from django import template

register = template.Library()

def match_third_party(links, third_party_name):
	return [l for l in links if l.third_party.name == third_party_name]

def match_category(links, category):
	return [l for l in links if l.category == category]


def get_soundcloud(links):
	return match_third_party(links, 'SoundCloud')

def get_residenta(links):
	return match_third_party(links, 'Resident Advisor')

def get_samples(links):
	return match_category(links, 'SMPL')

def get_representations(links):
	return match_category(links, 'REPR')




register.filter('soundcloud', get_soundcloud)
register.filter('residenta', get_residenta)
register.filter('smpl', get_samples)
register.filter('repr', get_representations)