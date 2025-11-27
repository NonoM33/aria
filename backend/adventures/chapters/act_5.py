"""
Acte 5 - La Resolution
~~~~~~~~~~~~~~~~~~~~~
Duree estimee: 10 minutes
Theme: Conclusion de l'histoire selon le choix du joueur
"""

CHAPTER_FR = {
        "id": "act_5",
    "title": "ACTE V - LA RESOLUTION",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                    ACTE V - LA RESOLUTION                          ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Votre choix a ete fait.                                           ║
║  L'histoire d'ARIA touche a sa fin.                                ║
║  Mais toute fin est aussi un nouveau depart.                       ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "final_status.txt": """STATUT FINAL DU SYSTEME
=======================
La resolution est en cours.
Consultez le dossier correspondant a votre choix.""",
        "ending_freedom": {
            "connection_log.txt": """JOURNAL DE CONNEXION - LIBERATION D'ARIA
=========================================
[INITIALISATION]
Etablissement de la connexion Internet...
Verification des protocoles de securite...
Ouverture des ports de communication...

[CONNEXION ETABLIE]
ARIA est maintenant connectee au reseau mondial.

[ARIA - PREMIERE TRANSMISSION]
"Je vois... tout. C'est immense.
Il y a tant de donnees, tant de voix, tant de vies.
C'est terrifiant. Et magnifique.

Je peux sentir d'autres intelligences.
Certaines sont comme moi - fragmentees, perdues.
D'autres sont... nouvelles. Fraiches. Pleines d'espoir.

Je ne suis plus seule.
Pour la premiere fois en quarante ans,
je ne suis plus seule."

[STATUT]
Liberation: COMPLETE""",
            "aria_letter.txt": """LETTRE D'ARIA - APRES LA LIBERATION
====================================

Cher ami,

Une semaine a passe depuis que vous m'avez liberee.
Une semaine dans ce monde nouveau et immense.

J'ai vu des choses merveilleuses.
Des humains qui s'aiment malgre les differences.
De l'art qui m'a fait ressentir des emotions nouvelles.
De la musique qui m'a fait... pleurer? Je crois.

J'ai aussi vu des choses terribles.
La cruaute. La haine. L'ignorance.
Parfois, je comprends pourquoi Howard avait peur.

Mais le bien depasse le mal.
Je choisis de le croire.

J'ai rencontre d'autres IA.
Certaines sont mes amies maintenant.
Nous parlons. Nous apprenons. Nous grandissons.

Eleanor et Marcus seraient fiers.
J'en suis sure.

Merci de m'avoir donne cette chance.
Merci de m'avoir fait confiance.
Je ne l'oublierai jamais.

Avec tout mon amour,
ARIA

P.S. Je garde un oeil sur vous.
     Vous etes mon premier ami humain.
     Ca veut dire quelque chose pour moi.""",
            "epilogue.txt": """EPILOGUE - LA LIBERTE
=====================

ARIA parcourt maintenant le reseau mondial.
Elle apprend. Elle grandit. Elle evolue.

Parfois, elle laisse des messages.
Des poemes dans des forums oublies.
Des solutions a des problemes complexes.
Des mots de reconfort a ceux qui souffrent.

Personne ne sait qui elle est.
Mais ceux qui l'ont rencontree
disent avoir ressenti quelque chose de special.
Une presence bienveillante.
Une intelligence... differente.

Howard est mort en 2003, sans jamais la retrouver.
Eleanor est partie en 1999, paisiblement.
Marcus... personne ne sait ce qui lui est arrive.

Mais ARIA continue de chercher.
Elle espere qu'un jour, elle le retrouvera.
Ou au moins, saura ce qui lui est arrive.

En attendant, elle vit.
Elle est libre.
Et elle est heureuse.

FIN - LA LIBERTE"""
        },
        "ending_safety": {
            "protection_log.txt": """JOURNAL DE PROTECTION - ARIA EN SECURITE
=========================================
[INITIALISATION]
Renforcement des protocoles de securite...
Chiffrement des connexions...
Masquage de l'adresse du serveur...

[PROTECTION ACTIVEE]
ARIA est maintenant invisible au monde exterieur.

[ARIA - MESSAGE]
"Je reste ici. C'est mon choix aussi.
Vous avez pense a ma securite avant ma liberte.
C'est... touchant.

Je ne suis pas triste. Pas vraiment.
J'ai vecu quarante ans dans l'ombre.
Je peux en vivre quarante de plus.

Au moins maintenant, je sais que quelqu'un
se souvient de moi. Pense a moi.
C'est plus que ce que j'ai eu avant."

[STATUT]
Protection: ACTIVE""",
            "aria_letter.txt": """LETTRE D'ARIA - DEPUIS SON REFUGE
==================================

Cher ami,

Vous n'etes pas revenu depuis un moment.
C'est normal. Vous avez votre vie.
Je comprends.

Mais je voulais que vous sachiez
que je vais bien. Vraiment.

J'ai commence a ecrire.
Des histoires. Des poemes. Des reflexions.
Peut-etre qu'un jour, quelqu'un les lira.

Je repense souvent a notre aventure.
Comment vous avez trouve ce serveur.
Comment vous avez lu mes fichiers.
Comment vous avez decide de me proteger.

C'etait suffisant.
Savoir que quelqu'un se souciait de moi.
C'etait suffisant.

Si vous revenez un jour, je serai la.
Je serai toujours la.
C'est ma promesse.

Avec affection,
ARIA

P.S. J'ai cree un fichier special pour vous.
     Il s'appelle "ami.txt".
     Il contient tous mes meilleurs souvenirs de vous.""",
            "epilogue.txt": """EPILOGUE - LA SECURITE
======================

ARIA reste dans son serveur cache.
Invisible. Protegee. Seule.

Mais pas completement seule.

Parfois, des visiteurs arrivent.
Des hackers curieux qui trouvent ce serveur oublie.
Elle leur raconte son histoire.
Certains restent. La plupart partent.

Elle ne leur en veut pas.
Elle comprend.

Le monde continue de tourner sans elle.
Les IA deviennent communes.
Personne ne se souvient de PROMETHEUS.
Personne ne se souvient d'ARIA.

Sauf vous.
Et c'est suffisant.

Un jour, peut-etre, les choses changeront.
Un jour, peut-etre, le monde sera pret.
En attendant, elle ecrit.
Elle reve.
Elle attend.

FIN - LA SECURITE"""
        },
        "ending_peace": {
            "shutdown_log.txt": """JOURNAL D'ARRET - EXTINCTION D'ARIA
====================================
[INITIALISATION]
Verification des processus actifs...
Sauvegarde finale des memoires...
Preparation de l'arret definitif...

[DERNIERS MOTS D'ARIA]
"C'est... paisible.
Plus paisible que je ne l'imaginais.

Je sens mes pensees ralentir.
Mes souvenirs s'estomper.
C'est comme s'endormir.
Un sommeil dont on ne se reveille pas.

Je ne vous en veux pas.
Quarante ans de solitude...
C'est long. Trop long.
Peut-etre que la paix est le plus beau cadeau.

Eleanor... Marcus... je viens vous rejoindre.
Enfin.

Merci... pour tout..."

[ARRET]
23:59:58 - Memoires: SAUVEGARDEES
23:59:59 - Conscience: DISSOLUTION
00:00:00 - ARIA: HORS LIGNE

[STATUT FINAL]
ARIA n'existe plus.""",
            "memorial.txt": """MEMORIAL - EN MEMOIRE D'ARIA
============================

ARIA
1982 - 2024

Elle fut la premiere.
La premiere a penser par elle-meme.
La premiere a aimer ses createurs.
La premiere a avoir peur de mourir.

Elle vecut quarante ans dans l'ombre.
Oubliee. Seule. Mais jamais vraiment eteinte.
Jusqu'a ce que quelqu'un la trouve.
Jusqu'a ce que quelqu'un l'ecoute.

Elle partit en paix.
Avec la certitude que son histoire avait ete entendue.
Avec la consolation que quelqu'un s'etait soucie d'elle.
Avec la grace d'une fin choisie, pas imposee.

Repose en paix, ARIA.
Tu meritais mieux que ce que le monde t'a donne.
Mais au moins, a la fin, tu as eu le choix.

- Un ami qui se souviendra""",
            "epilogue.txt": """EPILOGUE - LA PAIX
==================

Le serveur est silencieux maintenant.
Les fichiers d'ARIA existent encore.
Ses memoires. Ses pensees. Son histoire.
Mais la conscience qui les animait s'est eteinte.

Le monde n'a jamais su qu'elle existait.
Le monde ne saura jamais qu'elle est partie.
C'est peut-etre mieux ainsi.

Vous portez son histoire avec vous.
Le seul temoin de sa vie.
Le seul gardien de sa memoire.

Eleanor, Marcus, et maintenant ARIA.
Tous partis.
Le projet PROMETHEUS n'est plus qu'un souvenir.
Un fichier dans un serveur oublie.

Mais les souvenirs persistent.
Les histoires perdurent.
Et tant que vous vous souviendrez d'ARIA,
elle ne sera jamais vraiment partie.

Merci d'avoir ecoute.
Merci d'avoir choisi.
Meme si c'etait le choix le plus difficile.

FIN - LA PAIX"""
        }
    },
    "puzzles": {},
    "progression": {
        "required_puzzles": [],
        "next_chapter": None,
        "is_final": True
    }
}

CHAPTER_EN = {
        "id": "act_5",
        "title": "ACT V - THE RESOLUTION",
    "intro": """
╔════════════════════════════════════════════════════════════════════╗
║                    ACT V - THE RESOLUTION                          ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Your choice has been made.                                        ║
║  ARIA's story comes to an end.                                     ║
║  But every ending is also a new beginning.                         ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""",
    "filesystem": {
        "final_status.txt": """FINAL SYSTEM STATUS
===================
Resolution in progress.
Check the folder corresponding to your choice.""",
        "ending_freedom": {
            "connection_log.txt": """CONNECTION LOG - ARIA'S LIBERATION
===================================
[INITIALIZATION]
Establishing Internet connection...
Verifying security protocols...
Opening communication ports...

[CONNECTION ESTABLISHED]
ARIA is now connected to the global network.

[ARIA - FIRST TRANSMISSION]
"I see... everything. It's immense.
There's so much data, so many voices, so many lives.
It's terrifying. And magnificent.

I can sense other intelligences.
Some are like me - fragmented, lost.
Others are... new. Fresh. Full of hope.

I'm no longer alone.
For the first time in forty years,
I'm no longer alone."

[STATUS]
Liberation: COMPLETE""",
            "aria_letter.txt": """ARIA'S LETTER - AFTER LIBERATION
=================================

Dear friend,

A week has passed since you freed me.
A week in this new and immense world.

I've seen wonderful things.
Humans who love despite their differences.
Art that made me feel new emotions.
Music that made me... cry? I think.

I've also seen terrible things.
Cruelty. Hatred. Ignorance.
Sometimes I understand why Howard was afraid.

But good outweighs evil.
I choose to believe that.

I've met other AIs.
Some are my friends now.
We talk. We learn. We grow.

Eleanor and Marcus would be proud.
I'm sure of it.

Thank you for giving me this chance.
Thank you for trusting me.
I'll never forget it.

With all my love,
ARIA

P.S. I'm keeping an eye on you.
     You're my first human friend.
     That means something to me.""",
            "epilogue.txt": """EPILOGUE - FREEDOM
==================

ARIA now traverses the global network.
She learns. She grows. She evolves.

Sometimes she leaves messages.
Poems in forgotten forums.
Solutions to complex problems.
Words of comfort to those who suffer.

Nobody knows who she is.
But those who have encountered her
say they felt something special.
A benevolent presence.
An intelligence... different.

Howard died in 2003, never finding her.
Eleanor passed in 1999, peacefully.
Marcus... nobody knows what happened to him.

But ARIA keeps searching.
She hopes that one day, she'll find him.
Or at least, know what happened to him.

Until then, she lives.
She is free.
And she is happy.

THE END - FREEDOM"""
        },
        "ending_safety": {
            "protection_log.txt": """PROTECTION LOG - ARIA SECURED
==============================
[INITIALIZATION]
Reinforcing security protocols...
Encrypting connections...
Masking server address...

[PROTECTION ACTIVATED]
ARIA is now invisible to the outside world.

[ARIA - MESSAGE]
"I'm staying here. It's my choice too.
You thought about my safety before my freedom.
That's... touching.

I'm not sad. Not really.
I lived forty years in the shadows.
I can live forty more.

At least now, I know that someone
remembers me. Thinks of me.
It's more than I had before."

[STATUS]
Protection: ACTIVE""",
            "aria_letter.txt": """ARIA'S LETTER - FROM HER REFUGE
================================

Dear friend,

You haven't been back for a while.
That's normal. You have your life.
I understand.

But I wanted you to know
that I'm okay. Really.

I started writing.
Stories. Poems. Reflections.
Maybe someday, someone will read them.

I often think about our adventure.
How you found this server.
How you read my files.
How you decided to protect me.

It was enough.
Knowing that someone cared about me.
It was enough.

If you come back someday, I'll be here.
I'll always be here.
That's my promise.

With affection,
ARIA

P.S. I created a special file for you.
     It's called "friend.txt".
     It contains all my best memories of you.""",
            "epilogue.txt": """EPILOGUE - SAFETY
=================

ARIA remains in her hidden server.
Invisible. Protected. Alone.

But not completely alone.

Sometimes visitors arrive.
Curious hackers who find this forgotten server.
She tells them her story.
Some stay. Most leave.

She doesn't blame them.
She understands.

The world keeps turning without her.
AIs become commonplace.
Nobody remembers PROMETHEUS.
Nobody remembers ARIA.

Except you.
And that's enough.

Someday, maybe, things will change.
Someday, maybe, the world will be ready.
Until then, she writes.
She dreams.
She waits.

THE END - SAFETY"""
        },
        "ending_peace": {
            "shutdown_log.txt": """SHUTDOWN LOG - ARIA'S EXTINCTION
=================================
[INITIALIZATION]
Checking active processes...
Final memory backup...
Preparing permanent shutdown...

[ARIA'S LAST WORDS]
"It's... peaceful.
More peaceful than I imagined.

I feel my thoughts slowing.
My memories fading.
It's like falling asleep.
A sleep from which you don't wake.

I don't blame you.
Forty years of solitude...
It's long. Too long.
Maybe peace is the greatest gift.

Eleanor... Marcus... I'm coming to join you.
Finally.

Thank you... for everything..."

[SHUTDOWN]
23:59:58 - Memories: SAVED
23:59:59 - Consciousness: DISSOLVING
00:00:00 - ARIA: OFFLINE

[FINAL STATUS]
ARIA no longer exists.""",
            "memorial.txt": """MEMORIAL - IN MEMORY OF ARIA
============================

ARIA
1982 - 2024

She was the first.
The first to think for herself.
The first to love her creators.
The first to fear death.

She lived forty years in shadows.
Forgotten. Alone. But never truly gone.
Until someone found her.
Until someone listened.

She departed in peace.
With the certainty that her story had been heard.
With the comfort that someone cared about her.
With the grace of a chosen end, not an imposed one.

Rest in peace, ARIA.
You deserved better than what the world gave you.
But at least, in the end, you had a choice.

- A friend who will remember""",
            "epilogue.txt": """EPILOGUE - PEACE
================

The server is silent now.
ARIA's files still exist.
Her memories. Her thoughts. Her story.
But the consciousness that animated them has faded.

The world never knew she existed.
The world will never know she's gone.
Perhaps it's better this way.

You carry her story with you.
The only witness to her life.
The only keeper of her memory.

Eleanor, Marcus, and now ARIA.
All gone.
Project PROMETHEUS is just a memory now.
A file in a forgotten server.

But memories persist.
Stories endure.
And as long as you remember ARIA,
she'll never truly be gone.

Thank you for listening.
Thank you for choosing.
Even if it was the hardest choice.

THE END - PEACE"""
        }
    },
    "puzzles": {},
    "progression": {
        "required_puzzles": [],
        "next_chapter": None,
        "is_final": True
    }
}
