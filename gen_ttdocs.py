#!/usr/bin/env python

colors={
"RootTask": "#8dd3c7",
"DistributionTask": "#ffffb3",
"TrackVeteranTask": "#bebada",
"HearingTask": "#fb8072",
"ScheduleHearingTask": "#80b1d3",
"InformalHearingPresentationTask": "#fdb462",
"BvaDispatchTask": "#b3de69",
"EvidenceSubmissionWindowTask": "#fccde5",
"JudgeDecisionReviewTask": "#d9d9d9",
"AttorneyTask": "#bc80bd",
"JudgeAssignTask": "#ccebc5",
"HearingAdminActionVerifyAddressTask": "#ffed6f",
"AssignHearingDispositionTask": "#8dd3c7",
"EvidenceOrArgumentMailTask": "#ffffb3",
"TranslationTask": "#bebada",
"TranscriptionTask": "#fb8072",
"OtherColocatedTask": "#80b1d3",
"QualityReviewTask": "#fdb462",
"AttorneyRewriteTask": "#b3de69",
"TimedHoldTask": "#fccde5",
"AodMotionMailTask": "#d9d9d9",
"IhpColocatedTask": "#bc80bd",
"ScheduleHearingColocatedTask": "#ccebc5",
"VeteranRecordRequest": "#ffed6f",
"HearingRelatedMailTask": "#8dd3c7",
"JudgeDispatchReturnTask": "#ffffb3",
"MissingRecordsColocatedTask": "#bebada",
"FoiaTask": "#fb8072",
"GenericTask": "#80b1d3",
"ReturnedUndeliverableCorrespondenceMailTask": "#fdb462",
"NoShowHearingTask": "#b3de69",
"FoiaColocatedTask": "#fccde5",
"StayedAppealColocatedTask": "#d9d9d9",
"PowerOfAttorneyRelatedMailTask": "#bc80bd",
"HearingClarificationColocatedTask": "#ccebc5",
"ExtensionColocatedTask": "#ffed6f",
"PreRoutingFoiaColocatedTask": "#8dd3c7",
"HearingAdminActionForeignVeteranCaseTask": "#ffffb3",
"PoaClarificationColocatedTask": "#bebada",
"StatusInquiryMailTask": "#fb8072",
"PreRoutingTranslationColocatedTask": "#80b1d3",
"ExtensionRequestMailTask": "#fdb462",
"HearingAdminActionOtherTask": "#b3de69",
"CongressionalInterestMailTask": "#fccde5",
"ChangeHearingDispositionTask": "#d9d9d9",
"JudgeQualityReviewTask": "#bc80bd",
"PrivacyActTask": "#ccebc5",
"OtherMotionMailTask": "#ffed6f",
"SpecialCaseMovementTask": "#8dd3c7",
"VacateMotionMailTask": "#ffffb3",
"FoiaRequestMailTask": "#bebada",
"AddressVerificationColocatedTask": "#fb8072",
"AppealWithdrawalMailTask": "#80b1d3",
"ReconsiderationMotionMailTask": "#fdb462",
"AojColocatedTask": "#b3de69",
"AttorneyDispatchReturnTask": "#fccde5",
"AddressChangeMailTask": "#d9d9d9",
"AttorneyQualityReviewTask": "#bc80bd",
"TranslationColocatedTask": "#ccebc5",
"NewRepArgumentsColocatedTask": "#ffed6f",
"Task": "#8dd3c7",
"ControlledCorrespondenceMailTask": "#ffffb3",
"PrivacyActRequestMailTask": "#bebada",
"DeathCertificateMailTask": "#fb8072",
"BoardGrantEffectuationTask": "#80b1d3",
"PreRoutingMissingHearingTranscriptsColocatedTask": "#fdb462",
"ClearAndUnmistakeableErrorMailTask": "#b3de69",
"PendingScanningVbmsColocatedTask": "#fccde5",
"UnaccreditedRepColocatedTask": "#d9d9d9",
"PulacCerulloTask": "#bc80bd",
"MissingHearingTranscriptsColocatedTask": "#ccebc5",
"HearingAdminActionFoiaPrivacyRequestTask": "#ffed6f"
}


def gen_colors(inputfile):
    """
    Use this function to create the colors dict above.
    """

    import seaborn as sns

    typenames={}
    numappeals=0
    with open(inputfile) as jf:
        for linenum,line in enumerate(jf):
            try:
                data = json.loads(line)
                numappeals+=1
                for t in data['tasks']:
                    count=typenames.get(t['type'],0)
                    typenames[t['type']]=count+1
            except:
                print(f"Unexpected error at line {linenum}", line, sys.exc_info()[0])

    numtasks=sum(count for task,count in typenames.items())
    print("numappeals:", numappeals, " numtasks:", numtasks)
    sortednames=sorted(typenames.items(), key = lambda kv:(kv[1], kv[0]))
    sortednames.reverse()
    i=0
    for name,count in sortednames:
        print("\""+name+"\":cp["+str(i)+"],")
        i+=1


def rejectCancelled(data):
    return [t for t in data['tasks'] if not t['status']=="cancelled"]

def typesToStringUpTo(i, tcs):
    return ".".join(tcs[0:i+1])

appealIdsLimit=5
appealIdsDict={}
tcsCountsDict={}
tcsSetDict={}
nextlinksDict={}
backlinksDict={}

def flatten(data):
    taskscreationseq=list(map(lambda task: task['type']+"_"+task['assigned_to_type'], rejectCancelled(data)))
    for i in range(len(taskscreationseq)):
        task=taskscreationseq[i]
        if i>0:
            backlinksDict[task]=backlinksDict.get(task, {})
            backlinksDict[task][taskscreationseq[i-1]]=backlinksDict[task].get(taskscreationseq[i-1], 0)+1
        if i+1<len(taskscreationseq):
            nextlinksDict[task]=nextlinksDict.get(task, {})
            nextlinksDict[task][taskscreationseq[i+1]]=nextlinksDict[task].get(taskscreationseq[i+1], 0)+1
        
        typePrefix=typesToStringUpTo(i, taskscreationseq)
        
        tcsSetDict[task]=tcsSetDict.get(task, set())
        tcsSetDict[task].add(typePrefix)
        
        tcsCountsDict[typePrefix]=tcsCountsDict.get(typePrefix,0)+1
        
        appealIdsDict[typePrefix]=appealIdsDict.get(typePrefix, [])
        if(len(appealIdsDict[typePrefix])<appealIdsLimit):
            appealIdsDict[typePrefix].append(data['appeal_id'])

import json

def clearData():
    appealIdsDict.clear()
    tcsCountsDict.clear()
    tcsSetDict.clear()
    nextlinksDict.clear()
    backlinksDict.clear()

def loadData(inputfile, dockettype):
    clearData()
    #with open('prepped2.json', 'w') as pf:
    with open(inputfile) as jf:
        for count, line in enumerate(jf):
            try:
                data = json.loads(line)
                #removeExtraFields(data)
                if data['docket_type']==dockettype:
                    flatdata=flatten(data)
                #print(count, data['appeal_id'], flatdata)
                #pf.write(json.dumps(flatdata)+"\n")
            except:
                print(f"Unexpected error at line {linenum}", sys.exc_info()[0])

def create_tasklist(basedir, dockettype):
    with open(f'{basedir}/tasklist.md', 'w') as tlf:
        tlf.write(f'# Task Listing for "{dockettype}" Docket\n\n')
        listing={}
        for taskname,tcsSet in tcsSetDict.items():
            count=sum([tcsCountsDict[tcs] for tcs in tcsSet])
            listing[taskname]=count
        for taskname,count in sorted(listing.items(), key=lambda kv: kv[1], reverse=True):
            tlf.write(f'   * [{taskname}]({taskname}.md) ({count} occurrences)\n')

def gen_graphviz(nextlinksDict, backlinksDict, *tasknames):
    edges=set()
    for taskname in tasknames:
        if taskname in nextlinksDict:
            for link,count in sorted(nextlinksDict[taskname].items(), key=lambda kv: kv[1], reverse=True):
                edges.add(f'"{taskname}" -> "{link}" [label={count}]')
        if taskname in backlinksDict:
            for link,count in sorted(backlinksDict[taskname].items(), key=lambda kv: kv[1], reverse=True):
                edges.add(f'"{link}" -> "{taskname}" [label={count}]')
    gstr='digraph G {\nrankdir="LR";\n'
    gstr+="\n".join(edges)
    gstr+="\n}\n"
    return gstr

def save_graphviz(basedir, nextlinksDict, backlinksDict, *tasknames):
    tcsName=abbrev(".".join(tasknames))
    with open(f'{basedir}/dot/{tcsName}.dot', 'w') as gvf:
        gvf.write(gen_graphviz(nextlinksDict, backlinksDict, *tasknames))

def gen_plantuml(appeal, highlighttype="", limit=200):
    pstr = """@startuml
skinparam {
  ObjectBorderColor #555
  ObjectBorderThickness 0
  ObjectFontStyle bold
  ObjectFontSize 14
  ObjectAttributeFontColor #333
  ObjectAttributeFontSize 12
}
"""
    taskId2LabelDict={}
    for task in appeal['tasks']:
        taskLabel=f"{len(taskId2LabelDict)}.{task['type']}"
        taskId2LabelDict[task['id']]=taskLabel
        pstr+=f"  object {taskLabel} {colors[task['type']]}"
        pstr+=" {\n"
        pstr+=task['assigned_to_type']
        if task['type']+"_"+task['assigned_to_type']==highlighttype:
            pstr+=f"  <back:white>    </back>"
        pstr+="\n}\n"
    for task in appeal['tasks']:
        if task['parent_id']:
            pstr+=f"{taskId2LabelDict.get(task['parent_id'])} -- {taskId2LabelDict[task['id']]}\n"
    pstr+="@enduml\n"
    return pstr


import re
import sys

def find_appeal(inputfile, appeal_id):
    with open(inputfile, "r") as f:
        for count, line in enumerate(f):
            if re.search(f"\"appeal_id\":{appeal_id},", line):
                data = json.loads(line)
                return data

def abbrev(tcs):
    return ''.join(filter(lambda x: x.isupper() or x=='.', str(tcs)))

def gen_md_files(inputfile, basedir):
    print(f'\nCreating md files and associated dot and uml files under {basedir}')
    for taskname,tcsSet in tcsSetDict.items():
        #print(task, tcsSet)
        print(f'Creating {basedir}/{taskname}.md')
        with open(f'{basedir}/{taskname}.md', 'w') as mdf:
            #mdf.write('# '+taskname.split("_")[0]+" "+taskname.split("_")[1]+'\n\n')
            mdf.write('| [README.md](../README.md) | [Task Listing](tasklist.md) |\n\n')
            mdf.write(f'# {taskname}\n\n')
            
            mdf.write(f'[{taskname} description](../descr/{taskname}.md)\n\n')
            descfile=f'descr/{taskname}.md'
            if not os.path.exists(descfile):
                with open(descfile, 'w+') as descrf:
                    descrf.write(f'# {taskname} Description\n\n')
                    
            mdf.write(f'## Tasks Created Before and After\n\n')
            mdf.write(f"<details><summary>Tasks created before and after {taskname}</summary>\n\n```\n")
            graphviz=gen_graphviz(nextlinksDict, backlinksDict, taskname)
            mdf.write(graphviz)
            mdf.write('```\n</details>\n\n')
            mdf.write(f'![{taskname}](dot/{taskname}.dot.png)\n\n')
            with open(f'{basedir}/dot/{taskname}.dot', 'w') as gvf:
                gvf.write(graphviz)

            mdf.write('**Before:**\n\n')
            if taskname in backlinksDict:
                for link,count in sorted(backlinksDict[taskname].items(), key=lambda kv: kv[1], reverse=True):
                    mdf.write(f"   * [{link}]({link}.md): {count} times\n")
            mdf.write("\n")
            mdf.write('**After:**\n\n')
            if taskname in nextlinksDict:
                for link,count in sorted(nextlinksDict[taskname].items(), key=lambda kv: kv[1], reverse=True):
                    mdf.write(f"   * [{link}]({link}.md): {count} times\n")
            mdf.write("\n")

            mdf.write('## Task Creation Sequences\n\n')
            for tcs in sorted(tcsSet, key=lambda k: tcsCountsDict[k], reverse=True):
                mdf.write(gen_tcs_section(inputfile, basedir, taskname, tcs, tcsCountsDict[tcs], appealIdsDict[tcs]))

def gen_tcs_section(inputfile, basedir, taskname, tcs, count, example_appeal_ids):
    tcsName=abbrev(tcs)
    tstr=f"### {tcsName}\n\n"
    tstr+=(f'[{tcsName} description](../descr/{tcsName}.md)\n\n')
    #print(tcs.count('.'), tcs)
    if tcs.count('.') <= 3:
        descfile=f'descr/{tcsName}.md'
        #print("Creating", tcs)
        if not os.path.exists(descfile):
            with open(descfile, 'w+') as descrf:
                descrf.write(f'# {tcsName} Description\n\n')       
    
    tstr+=f"{count} occurrences (example appeal IDs: {example_appeal_ids})\n\n"
    appealId=appealIdsDict[tcs][0]
    tstr+=f"<details><summary>Task Tree for appeal with ID {appealId}</summary>\n\n```\n"
    appeal=find_appeal(inputfile, appealId)
    plantuml=gen_plantuml(appeal, taskname)
    tstr+=plantuml
    tstr+='```\n</details>\n\n'
    
    tstr+=f'![{tcsName}-{appealId}](uml/{tcsName}-{appealId}.png)\n\n'
    # create associated plantUML file to generate png
    with open(f'{basedir}/uml/{tcsName}-{appealId}.uml', 'w') as umlf:
        umlf.write(plantuml)
        
    return tstr


import os
def generate_docs(inputfile):
    os.path.isdir('descr') or os.mkdir('descr')

    dockettypes={ "direct_review":"docs-DR", "evidence_submission":"docs-ES", "hearing":"docs-H" }
    for dockettype,basedir in dockettypes.items():
        loadData(inputfile, dockettype)

        os.path.isdir(basedir) or os.mkdir(basedir)
        os.path.isdir(basedir+'/uml') or os.mkdir(basedir+'/uml')
        os.path.isdir(basedir+'/dot') or os.mkdir(basedir+'/dot')

        create_tasklist(basedir, dockettype)
        gen_md_files(inputfile, basedir)
        
        
def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <input.json>")
        sys.exit(0)

    print(f'Processing {sys.argv[1]}')
    generate_docs(sys.argv[1])

    print("\nNext step: run createPngs.sh to convert dot and uml into images referenced by md files.")

if __name__ == "__main__":
    main()


