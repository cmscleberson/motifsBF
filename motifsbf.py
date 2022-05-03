from itertools import combinations_with_replacement, combinations, permutations
import os.path
import itertools


def generateList(listWord):
    listOut = []
    listTemp = []
    for i in range(len(listWord)):
        for j in range(len(listWord[i])):
            for k in range(len(listWord[i][j])):
                listTemp.append(listWord[i][j][k].lower())
        listOut.append(listTemp.copy())
        listTemp.clear()
    return listOut


def newList():
    listCl = []
    for i in range(0, 27):
        listCl.append(0)
    return listCl


def identOccur(regsList):
    regsOccurrences = []
    regsValues = []
    listOccFinal = []

    for i in range(97, 124):
        regsValues.append(i)
        regsOccurrences.append(0)

    for i in range(len(regsList)):
        listOcc = newList()

        for j in range(len(regsList[i])):
            local = ord(regsList[i][j])
            for k in range(len(regsValues)):
                if regsValues[k] == local:
                    listOcc[k] = 1
        listOccFinal.append(listOcc.copy())

    return listOccFinal


def countOccur(listOccur):
    listCount = newList()

    for i in range(len(listOccur)):
        lines = len(listOccur)
        for j in range(len(listOccur[i])):
            cols = j

        for k in range(cols):

            countOcc = 0
            for l in range(len(listOccur)):

                if listOccur[l][k] == 1:
                    countOcc = countOcc + 1
            if countOcc == lines:
                listCount[k] = 1

    return listCount


def strRepList(listCount):
    listOutStr = []

    for i in range(len(listCount)):
        if listCount[i] == 1:
            listOutStr.append(chr(i + 97))

    return listOutStr


def getStrsEachSeq(listOrig, listOccur):

    listOut = []
    listAux_1 = []
    listAux_2 = []
    listAux = []
    idx = 0
    listIdx = []
    listIdxTemp =[]
    for i in range(len(listOrig)):
        for j in range(len(listOrig[i])):
            for itIn in range(len(listOccur)):

                if listOrig[i][j] == listOccur[itIn]:
                    vlIn = listOrig[i][j]
                    listAux_1.append(vlIn)


        listOut.append(listAux_1.copy())
        listAux_1.clear()

    return listOut


def genMers(listFreqSeq):

    listMers = []
    listTempMers = []

    size = 1
    for i in range(len(listFreqSeq)):
        bg = 0
        listLen = len(listFreqSeq[i])+1
        for bg in range(len(listFreqSeq[i])):
            for j in range(listLen):
                if j> bg:
                    listTempMers.append(listFreqSeq[i][bg:j])


        listMers.append(listTempMers.copy())
        listTempMers.clear()

    return listMers





def findMotifs(listInMers):
    name_of_file = 'listMotifs'
    save_path = os.getcwd() + '/'

    completeName = os.path.join(save_path, name_of_file + ".txt")
    file = open(completeName, "w")

    lstMot = []
    lstMotOut= []

    for j in range(len(listInMers[0])):
        itVl = listInMers[0][j]

        count = 0

        for p in range(1,len(listInMers)):
            for q in range(len(listInMers[p])):

                if itVl == listInMers[p][q]:
                    count = count+1


            if count >= len(listInMers)-1:
                lstMot.append(itVl)


    for q in range(len(lstMot)):
        if lstMot[q] not in lstMotOut:
            lstMotOut.append(lstMot[q])
            file.write(str(lstMot[q]))
            file.write('\n')

    file.close()



            




listTest01 = [["MAKNITVPYVSVSDFDWGLNLEASASLPWNPTIWSLVAALTALPLWMTLELTVSVLYVFQRWSGLYFYAVLITAWSISLHAIGFLLSYCVPSCNWIASSIMTELGWVGMVTGFSLVLYSRLNLMSFIMRNRHISRIALAMIITNAVLFHIPTFVVFMIGVSSPGLFVKYISAMNALERVQIVMFSVQELILSGLYIYGTFKMAQDSFNSRIRRTI"],


["MATNITVPYVAIGDFDWGLNLASSVPLPWNQTIWSLVAVFTALPLWMTLELTVSVLYVFRRWSGLYFWAVLVTTWSISLHAIGFLLSYCVPSCNWIASSLITEFGWAGMVTGFSLVLYSRLTLLSFVMRNRHISRIALGMITTDAILFHIPTFVVFMVGISSPANFVKYVPYMNIVERIQIVMFSVQELILSGLYIYGTFKMAQDSFNSRIRRTI"],


["MADLPKLRSLVAAFTALPLWMTIELTVSVLYVFRRWSGLYFWSVLVTTWSISVHAIGFLLSYCVPSCNQIASSVLAEVGWVGMVSGFAVVLYSRLNLISFVMQNRHILRLALGMIITDAMLFHIPALVIFIIGTSSGAMFEKYVTCMNILERIQIVAFSVQELIISGLYIYGTFKMERDSFNSRIRKTIRLLITVQIAVILCDALLITLDFAGYY"],



["MAENITVPYVPFDQFHWSISYTGPLPWNQTVWSLIAVFTALPLWMTVELTVWVFYLFRRWSGLYFWSVLITTWGVTLHAIGFVLKVCVPRCNYILSMVIAELGWIGMVTGFAMVMYSRLNLIGFVMRNRYILRLALAMIIVDGIVFHTSTITIFAIGLANPSARYLSYMNAIERVQIVIFTVQEIILSVIYIYGTFKMAQDSFNNRIRSTINYLI"],


["MAGNITVPYVPFDQFHWSMSHVGPLPWNQTVWSLIAVFTALPLWITIELTICVFYLFRRWSGLYFWSVLITTWGVTLHAIGFVLKVCVPSCNYIFSMVVAELGWMGMVTGFAMVMYSRLSLIGFVMRNRYILRLALAMIIINAIVLHTSTITIFAIGIEEPGPKYLSYMNSIERIQIVIFTVQEVILSTIYIYGTFKMAQDSFNKRIRATISYLI"],

["MTSVRNITVPYVPLDEFDWSFYRSGPLPWNQTIWSLIAVFTAVPLWMTIELTVWVFYIFNRYSGLYFWSVLITTWGVTLHAIGFVLKDCVPQCSWIFSTILAEIGWVGMVTGFSVVLYSRLHLVSFVMHSSSILRLALSMIIIDALLFHVPTIVFQFGCSDPHTHAKYVAYMGPMERVQVLGFSIQETILSALYIYGTVQMFKESITSKIRTTLK"],


["MSGLHNITVPYVSTSQFDWSFARTYPLPWNQTIWSIVAVFSAVPLWMNIELTVWVLYVFRRYSGLYFWSILITTWCIALHAIGYVLKECVPDCNWILSTLIVEIGWVGMVTGFSMVLYSRLHLVNFTIKNPHILRITLIMIITDAFLFHTPTIVFQFGLANQSRHDQYASYLHVMERIQIMGFSLQEITLTSIYIYGTLQIIKSSLNSKIRTTMV"],


["MTKVHNITVPYVTVSDFDWSFARTGPLPWNQTVWSLIAVFTALPLWTTIELTVCVFYTFRRYSGLYFWSVLCTTWGVTIHAIGFVLKFCVPSCNWIFSTVLAEIGWVGMVSGFSIVLYSRLHLVVRSQRTLQLVLAAIVVDAFLFHVPTIVFQFGTSDKHTHKKFLPYMNVMERVQIVGFSVQEIIISAIYIYATMQMLRGSFNRRMRTTMAWLI"],


["MSVHNITVPYVNVIDFDWGFNRTGPLPWNQTVWSILAVFTAVPLWMTVELTIWVFYVFRRWSGLYFWSVLICTWGVTLHTIGFILKFCVPSCNWIVSTTLAEIGWVSMVTGFSVVLYSRLHLVVRSPRILNLVLIMVMTDAFLFHVPTIVFQYGISANGKTHVYYLPFMAPMERIQVFGFSIQEVVISIIYIWATLRMLKGSFNKKIRNTIIFLI"],



["MAEECVHFVKFSDYDWTFDRVGWLPWNPAAFCLIAAVCAIAYWMSIEVLVLVYVTFKRHAGIYFWSIIFTTIGIILQNTGYILLSFENTWPVILVVVICKIGWIMNVTGFSIVLWSRLHLVVRSQRILKWLLVIILIDGLVCHTPIAVFEFGLMTRNHNTYYRPMQIMERIQQTVFTIQETIMSCLYIYHTRKFLKIGYPMQTRKVVGLLLLVQL"]]

listTest = [['kmgctpmtdcpfstribacfindingcasa'],['tddicptriatbcasamgcdplplfindingabbc'],['tricasamactcpmgtnafindingtdpopicab']]
'''
Planted motifs:
mg
td
cp
tri
casa
finding
'''


lst = generateList(listTest)
lstOcc = identOccur(lst)
lstCountOc = countOccur(lstOcc)
lstStr = strRepList(lstCountOc) #list os residues found in all sequences
lstStrEachSeq = getStrsEachSeq(lst, lstStr)

print('\nGenerating mers .......')
lstMers = genMers(lstStrEachSeq)
print('\nFinding motifs .......')
findMotifs(lstMers)


print('\nDone!!!!!!!!!!!')

