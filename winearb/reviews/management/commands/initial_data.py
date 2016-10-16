# coding=utf-8

from django.core.management.base import BaseCommand
from winearb.reviews.models import Review, Wine
from winearb.upload_handling.models import WineImage
from winearb.users.models import User

class Command(BaseCommand):

    help = 'Populates initial WineArb data'

    def will_ciel(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/2011 Ciel-250.png'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 16
        comment = """Tasted with Jason one late night after closing at Northside...
                     Muted on the nose initially, but eventually notes of mocha and cassis emerged.
                     On the palate though, wow. Compelling texture. Gravelly tannins. Backward for
                     sure, and too austere for most (it was for Jason), but ever since this tasting
                     I have never been able to forget about... Red Mountain."""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def lalande_borie(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/62480b.png'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 12
        comment = """Bought this from Jeff at an artificially low cost price (Oops),
                     but this review reflects my opinion had I paid market price.
                     Great wine. Big, new world style. Very polished, never over the top. Lacks typicity."""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def desclau(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/145894.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 20
        comment = """All the typicity you could ever ask for. Pencil, cassis, blackberry,
                     structure, balance, TONS of sediment. This is Bordeaux. This is arbitrage.
                     A wine that CLEARLY communicates a sense of place (Bordeaux no less), for $12?!?
                     That's already a max score. Why do you think you can no longer find it?"""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def palmer(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/179968.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 15
        comment = """Tasted with Sarah at a Beverly Hills art gallery. Wine of the day by a mile.
                     Drinking much better than the off-vintage Ducrus and the '09/'10 Haut-Brions, by a mile."""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def pavie(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/734845.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 7
        comment = """Not much to say here. I have and will continue to (successfully) turn customers onto better values than this."""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def moncayo(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/1188046x.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 17
        comment = """Big and bold beast of a wine that remains impeccably balanced over the 3-day drinking window
                     you have after opening it. Coffee, black fruit, full body, and lingering. Coats the glass. Best
                     without food and slightly chilled."""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def amapola(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/1271947x.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 6
        comment = """PnP. Screams 'Cabernet Sauvignon' from start to finish. Complex nose of mint, blueberry, stewed dark fruit and herbs.
                     Tastewise, this is a bit of a letdown. Very down the middle, uninteresting, and unbalanced.
                     I also expected a little more in the texture department (grippy but thats it).
                     Maybe this comes around in a year or two?"""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def closdepapes(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/2544486a-7320-11e5-913e-657592d1d4ee.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 7
        comment = """Had a pour at Wally's with a Kobe burger. This guy just seemed to fall a bit flat for the money,
                     but you can still tell that it is a solid wine. The bottle may have been open for a while."""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def desmirail(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/bor957_1.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 18
        comment = """Phenomenal Margaux. Flowers, lead, red fruits. Lean and silky on the palate, with mouth-coating
                     tannins. Just kept getting better as we went through the bottle."""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def lra(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/bot-lariojaalta-904-2005.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 19
        comment = """This is what Spanish wine is all about: value at all price levels. One of the most
                     balanced wines I have ever had, and would be my first choice for ANY food pairing. It
                     ENVELOPS and ENHANCES the food (I was snacking on a bunch of stuff around the house).
                     All this being said, if you drink now, decant for at least an hour, preferably more."""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def masblau(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/bot-mascanblau-2012.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 10
        comment = """A real crowd-pleaserm though I prefer something a bit more interesting at this price point."""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def canblau(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/CAN-BLAU-MONTSANT-750ML.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 15
        comment = """What you want and expect at this price point. You get all those hedonistic Spanish wine qualities
                     at a daily-drinker cost."""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def plaisance(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/Emilion-Gran_1024x1024.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 18
        comment = """The right-bank, higher-priced version of Desclau. I came into work one morning and found that we had a
                     bottle opened from the previous night, so I gave it a try. Juicy, ripe, funky and tannic,
                     in the way only the Bordelaise know how to do it. What I recommend you get instead of Esprit Pavie."""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def dofi(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/Finca Dofí 2004.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 15
        comment = """PnP. A gift (for what I paid) from Jeff, and shared with Sarah and Christian. Gorgeous black wine with a fascinating array of black and blue fruits on the nose and palate.
                     Texture goes from lush and polished to grippy and lingering. The highlight, for me,
                     is the sophisticated fruit profile this displays... Simply classy stuff. But would I pay $120 for it?"""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def aubin(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/IMG_3764-1024x462.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 3
        comment = """Yeah yeah, I know. PYCM is STILL one of the best bargains on the Cote d'Or, and yeah,
                     Saint-Aubin has become one of the best bargains on the Cote d'Or. This wine is comically
                     unbalanced. Acid and Oak... that's all folks."""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def pycmchass(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/P02546.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 14
        comment = """Great Chassagne-Montrachet from a quality producer. Great now and getting better."""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def tour(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/tour-haut-caussan-label.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 15
        comment = """Jeff and I were at the tasting for this importer, and towards the end we discussed wines of
                     the day, price books in hand. He looked at his illegible nonsense, and I looked at mine. We both had illegible nonsense next to this wine, so
                     we knew we both liked it, and bought a few cases. The wine reminds me of a burning forest."""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def pichon(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/vin-rouge-chateau-pichon-longueville-baron-2eme-grand-cru-classe-2000-75cl-3.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 17
        comment = """What you expect from Bordeaux at this level. 'Woven red and black' is what I like to
                     describe it as. Tannins cling to all parts of mouth. Appealing."""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()

    def alberdi(self):
        review = Review()
        review.save()
        user = User.objects.get(username='robert')
        uploaded_file = 'initial_photos/vina_alberdi__15168.jpg'
        image = WineImage(shot=uploaded_file,
                          user=user,
                          review=review)
        rating = 17
        comment = """2nd place wine from our Rioja reserva tasting at Northside. Jasoon and I knew it was good, and it
                     ended up outselling the winner. This wine is what started my appreciation for Rioja, and Spain
                     in general. Notes of cranberry, vanilla and iron on the nose. The palate reflects the nose.
                     Generous acidity for food matches. I personally went with smoked country pork ribs slathered with
                     sauce made from this very wine. Versatile?"""
        review.user_name = user.username
        review.rating = rating
        review.comment = comment
        review.save()
        image.save()




    def handle(self, *args, **options):
        self.will_ciel()
        self.lalande_borie()
        self.desclau()
        self.palmer()
        self.pavie()
        self.moncayo()
        self.amapola()
        self.closdepapes()
        self.desmirail()
        self.lra()
        self.masblau()
        self.canblau()
        self.plaisance()
        self.dofi()
        self.aubin()
        self.pycmchass()
        self.tour()
        self.pichon()
        self.alberdi()
