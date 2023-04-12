import bcrypt

def crypt_mdp(mdp):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(mdp.encode('utf-8'), salt)
    return hashed


def match_mdp(mdp, hashed):
    if bcrypt.checkpw(mdp.encode('utf-8'), hashed.encode('utf-8')):
        return True
    else:
        return False
