def pipeline_2(listes,*argslambda):
    for lambdaf in argslambda : 
        listes = [lambdaf(x) for x in listes]