#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on maart 29, 2024, at 16:31
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
import pandas as pd
# Set number of trials you want to show for practice/main parts of experiment
nPract = 10
nMain = 10

nTotal = nPract + nMain
# Load all possible conditions from triplets.csv
df = pd.read_csv('triplets.csv')
sampled = df.sample(nTotal)
# Sample practice trials and main trials
samplePract = sampled[:nPract]
sampleMain = sampled[nPract:nTotal]
# Store these trials in separate files that are to be used later on
samplePract.to_csv('practice_triplets.csv', index=False)
sampleMain.to_csv('main_triplets.csv', index=False)


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'odd_one_out_experiment'  # from the Builder filename that created this script
expInfo = {
    'participant': '0000',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/' + expInfo['participant'] + '/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\tomva\\OneDrive\\KU Leuven\\Master Theory and Research\\StudentJob\\Triplet similarity experiment\\triplet-similarity-experiment\\test\\odd_one_out_experiment_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "welcome" ---
welcomeText = visual.TextStim(win=win, name='welcomeText',
    text="Welcome, in this experiment you will be presented with three chess scenario's, side-by-side.\n\nIt is your task to select the odd-one-out. In other words, choose the one you think is the most different when comparing to the other two scenario's.\n\nTo select the odd-one-out you can use your mouse. Click on the scenario you think is the most distinct. \n\nWe will first show you an example of a single trial. It is not necessary to pay attention to the correctness of the decision, rather focus on the general lay-out of the task.\n\nAfter the example you can practice the task yourself.\n\nPress <space> to continue...",
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "example" ---
instr_image = visual.ImageStim(
    win=win,
    name='instr_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.7, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=256.0, interpolate=True, depth=0.0)
text = visual.TextStim(win=win, name='text',
    text="Let's say you think the most distinct scenario is the one in the middle.\nYou can then use your mouse to select this specific scenario as the odd-one-out. \n\nPress <space> to continue to the practice trials...",
    font='Open Sans',
    pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_example = keyboard.Keyboard()

# --- Initialize components for Routine "practice" ---
fixation_practice = visual.ShapeStim(
    win=win, name='fixation_practice', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
frame1 = visual.Rect(
    win=win, name='frame1',
    width=(0.45, 0.45)[0], height=(0.45, 0.45)[1],
    ori=0.0, pos=(-0.5, 0), anchor='center',
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-1.0, interpolate=True)
frame2 = visual.Rect(
    win=win, name='frame2',
    width=(0.45, 0.45)[0], height=(0.45, 0.45)[1],
    ori=0.0, pos=(0,0), anchor='center',
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-2.0, interpolate=True)
frame3 = visual.Rect(
    win=win, name='frame3',
    width=(0.45, 0.45)[0], height=(0.45, 0.45)[1],
    ori=0.0, pos=(0.5, 0), anchor='center',
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-3.0, interpolate=True)
stim1_pract = visual.ImageStim(
    win=win,
    name='stim1_pract', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
stim2_pract = visual.ImageStim(
    win=win,
    name='stim2_pract', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
stim3_pract = visual.ImageStim(
    win=win,
    name='stim3_pract', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
mouse_pract = event.Mouse(win=win)
x, y = [None, None]
mouse_pract.mouseClock = core.Clock()
question_text = visual.TextStim(win=win, name='question_text',
    text='Which is the odd-one-out?',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "pause" ---
pauseText = visual.TextStim(win=win, name='pauseText',
    text="We have finished practicing!\n\nLet's start with the experiment, the task remains the same as it was during practice.\n\nPress <space> to continue...",
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_pause = keyboard.Keyboard()

# --- Initialize components for Routine "experiment" ---
fixation_main = visual.ShapeStim(
    win=win, name='fixation_main', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
frame1_main = visual.Rect(
    win=win, name='frame1_main',
    width=(0.45, 0.45)[0], height=(0.45, 0.45)[1],
    ori=0.0, pos=(-0.5, 0), anchor='center',
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-1.0, interpolate=True)
frame2_main = visual.Rect(
    win=win, name='frame2_main',
    width=(0.45, 0.45)[0], height=(0.45, 0.45)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-2.0, interpolate=True)
frame3_main = visual.Rect(
    win=win, name='frame3_main',
    width=(0.45, 0.45)[0], height=(0.45, 0.45)[1],
    ori=0.0, pos=(0.5, 0), anchor='center',
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-3.0, interpolate=True)
stim1_main = visual.ImageStim(
    win=win,
    name='stim1_main', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
stim2_main = visual.ImageStim(
    win=win,
    name='stim2_main', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
stim3_main = visual.ImageStim(
    win=win,
    name='stim3_main', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
mouse_main = event.Mouse(win=win)
x, y = [None, None]
mouse_main.mouseClock = core.Clock()
question_text_2 = visual.TextStim(win=win, name='question_text_2',
    text='Which is the odd-one-out?',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "exit" ---
text_exit = visual.TextStim(win=win, name='text_exit',
    text='That was it!\n\nThank you for your time and attention.\n\nPress <space> to leave the experiment.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
welcomeComponents = [welcomeText, key_resp]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeText* updates
    if welcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeText.frameNStart = frameN  # exact frame index
        welcomeText.tStart = t  # local t and not account for scr refresh
        welcomeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcomeText.started')
        welcomeText.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcome" ---
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "example" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_example.keys = []
key_example.rt = []
_key_example_allKeys = []
# keep track of which components have finished
exampleComponents = [instr_image, text, key_example]
for thisComponent in exampleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "example" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_image* updates
    if instr_image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instr_image.frameNStart = frameN  # exact frame index
        instr_image.tStart = t  # local t and not account for scr refresh
        instr_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_image.started')
        instr_image.setAutoDraw(True)
    if instr_image.status == STARTED:  # only update if drawing
        instr_image.setImage('instructFrame1.png', log=False)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_example* updates
    waitOnFlip = False
    if key_example.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_example.frameNStart = frameN  # exact frame index
        key_example.tStart = t  # local t and not account for scr refresh
        key_example.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_example, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_example.started')
        key_example.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_example.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_example.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_example.status == STARTED and not waitOnFlip:
        theseKeys = key_example.getKeys(keyList=['space'], waitRelease=False)
        _key_example_allKeys.extend(theseKeys)
        if len(_key_example_allKeys):
            key_example.keys = _key_example_allKeys[-1].name  # just the last key pressed
            key_example.rt = _key_example_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exampleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "example" ---
for thisComponent in exampleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_example.keys in ['', [], None]:  # No response was made
    key_example.keys = None
thisExp.addData('key_example.keys',key_example.keys)
if key_example.keys != None:  # we had a response
    thisExp.addData('key_example.rt', key_example.rt)
thisExp.nextEntry()
# the Routine "example" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practiceTrials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice_triplets.csv'),
    seed=None, name='practiceTrials')
thisExp.addLoop(practiceTrials)  # add the loop to the experiment
thisPracticeTrial = practiceTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
if thisPracticeTrial != None:
    for paramName in thisPracticeTrial:
        exec('{} = thisPracticeTrial[paramName]'.format(paramName))

for thisPracticeTrial in practiceTrials:
    currentLoop = practiceTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial:
            exec('{} = thisPracticeTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "practice" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    stim1_pract.setImage('../datasets/fmri_dataset/images/' + Stim1)
    stim2_pract.setImage('../datasets/fmri_dataset/images/' + Stim2)
    stim3_pract.setImage('../datasets/fmri_dataset/images/' + Stim3)
    # setup some python lists for storing info about the mouse_pract
    mouse_pract.x = []
    mouse_pract.y = []
    mouse_pract.leftButton = []
    mouse_pract.midButton = []
    mouse_pract.rightButton = []
    mouse_pract.time = []
    mouse_pract.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    practiceComponents = [fixation_practice, frame1, frame2, frame3, stim1_pract, stim2_pract, stim3_pract, mouse_pract, question_text]
    for thisComponent in practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_practice* updates
        if fixation_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_practice.frameNStart = frameN  # exact frame index
            fixation_practice.tStart = t  # local t and not account for scr refresh
            fixation_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_practice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_practice.started')
            fixation_practice.setAutoDraw(True)
        if fixation_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_practice.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_practice.tStop = t  # not accounting for scr refresh
                fixation_practice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_practice.stopped')
                fixation_practice.setAutoDraw(False)
        
        # *frame1* updates
        if frame1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            frame1.frameNStart = frameN  # exact frame index
            frame1.tStart = t  # local t and not account for scr refresh
            frame1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(frame1, 'tStartRefresh')  # time at next scr refresh
            frame1.setAutoDraw(True)
        if frame1.status == STARTED:  # only update if drawing
            frame1.setOpacity(None, log=False)
        
        # *frame2* updates
        if frame2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            frame2.frameNStart = frameN  # exact frame index
            frame2.tStart = t  # local t and not account for scr refresh
            frame2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(frame2, 'tStartRefresh')  # time at next scr refresh
            frame2.setAutoDraw(True)
        if frame2.status == STARTED:  # only update if drawing
            frame2.setOpacity(None, log=False)
        
        # *frame3* updates
        if frame3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            frame3.frameNStart = frameN  # exact frame index
            frame3.tStart = t  # local t and not account for scr refresh
            frame3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(frame3, 'tStartRefresh')  # time at next scr refresh
            frame3.setAutoDraw(True)
        if frame3.status == STARTED:  # only update if drawing
            frame3.setOpacity(None, log=False)
        
        # *stim1_pract* updates
        if stim1_pract.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stim1_pract.frameNStart = frameN  # exact frame index
            stim1_pract.tStart = t  # local t and not account for scr refresh
            stim1_pract.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim1_pract, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stim1_pract.started')
            stim1_pract.setAutoDraw(True)
        
        # *stim2_pract* updates
        if stim2_pract.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stim2_pract.frameNStart = frameN  # exact frame index
            stim2_pract.tStart = t  # local t and not account for scr refresh
            stim2_pract.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim2_pract, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stim2_pract.started')
            stim2_pract.setAutoDraw(True)
        
        # *stim3_pract* updates
        if stim3_pract.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stim3_pract.frameNStart = frameN  # exact frame index
            stim3_pract.tStart = t  # local t and not account for scr refresh
            stim3_pract.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim3_pract, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stim3_pract.started')
            stim3_pract.setAutoDraw(True)
        # *mouse_pract* updates
        if mouse_pract.status == NOT_STARTED and t >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            mouse_pract.frameNStart = frameN  # exact frame index
            mouse_pract.tStart = t  # local t and not account for scr refresh
            mouse_pract.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_pract, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_pract.started', t)
            mouse_pract.status = STARTED
            mouse_pract.mouseClock.reset()
            prevButtonState = mouse_pract.getPressed()  # if button is down already this ISN'T a new click
        if mouse_pract.status == STARTED:  # only update if started and not finished!
            buttons = mouse_pract.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([stim1_pract, stim2_pract, stim3_pract])
                        clickableList = [stim1_pract, stim2_pract, stim3_pract]
                    except:
                        clickableList = [[stim1_pract, stim2_pract, stim3_pract]]
                    for obj in clickableList:
                        if obj.contains(mouse_pract):
                            gotValidClick = True
                            mouse_pract.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = mouse_pract.getPos()
                        mouse_pract.x.append(x)
                        mouse_pract.y.append(y)
                        buttons = mouse_pract.getPressed()
                        mouse_pract.leftButton.append(buttons[0])
                        mouse_pract.midButton.append(buttons[1])
                        mouse_pract.rightButton.append(buttons[2])
                        mouse_pract.time.append(mouse_pract.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *question_text* updates
        if question_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            question_text.frameNStart = frameN  # exact frame index
            question_text.tStart = t  # local t and not account for scr refresh
            question_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_text, 'tStartRefresh')  # time at next scr refresh
            question_text.setAutoDraw(True)
        # Run 'Each Frame' code from code_pract
        # Get mouse position
        mouseX, mouseY = mouse_pract.getPos()
        
        if stim1_pract.contains(mouseX, mouseY):
            frame1.opacity = 1
        else:
            frame1.opacity = 0
            
        if stim2_pract.contains(mouseX, mouseY):
            frame2.opacity = 1
        else:
            frame2.opacity = 0
            
        if stim3_pract.contains(mouseX, mouseY):
            frame3.opacity = 1
        else:
            frame3.opacity = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice" ---
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practiceTrials (TrialHandler)
    practiceTrials.addData('mouse_pract.x', mouse_pract.x)
    practiceTrials.addData('mouse_pract.y', mouse_pract.y)
    practiceTrials.addData('mouse_pract.leftButton', mouse_pract.leftButton)
    practiceTrials.addData('mouse_pract.midButton', mouse_pract.midButton)
    practiceTrials.addData('mouse_pract.rightButton', mouse_pract.rightButton)
    practiceTrials.addData('mouse_pract.time', mouse_pract.time)
    practiceTrials.addData('mouse_pract.clicked_name', mouse_pract.clicked_name)
    # the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practiceTrials'

# get names of stimulus parameters
if practiceTrials.trialList in ([], [None], None):
    params = []
else:
    params = practiceTrials.trialList[0].keys()
# save data for this loop
practiceTrials.saveAsText(filename + 'practiceTrials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "pause" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_pause.keys = []
key_resp_pause.rt = []
_key_resp_pause_allKeys = []
# keep track of which components have finished
pauseComponents = [pauseText, key_resp_pause]
for thisComponent in pauseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "pause" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pauseText* updates
    if pauseText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pauseText.frameNStart = frameN  # exact frame index
        pauseText.tStart = t  # local t and not account for scr refresh
        pauseText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pauseText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pauseText.started')
        pauseText.setAutoDraw(True)
    
    # *key_resp_pause* updates
    waitOnFlip = False
    if key_resp_pause.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_pause.frameNStart = frameN  # exact frame index
        key_resp_pause.tStart = t  # local t and not account for scr refresh
        key_resp_pause.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_pause, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_pause.started')
        key_resp_pause.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_pause.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_pause.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_pause.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_pause.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_pause_allKeys.extend(theseKeys)
        if len(_key_resp_pause_allKeys):
            key_resp_pause.keys = _key_resp_pause_allKeys[-1].name  # just the last key pressed
            key_resp_pause.rt = _key_resp_pause_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pause" ---
for thisComponent in pauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pause" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
mainTrials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('main_triplets.csv'),
    seed=None, name='mainTrials')
thisExp.addLoop(mainTrials)  # add the loop to the experiment
thisMainTrial = mainTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMainTrial.rgb)
if thisMainTrial != None:
    for paramName in thisMainTrial:
        exec('{} = thisMainTrial[paramName]'.format(paramName))

for thisMainTrial in mainTrials:
    currentLoop = mainTrials
    # abbreviate parameter names if possible (e.g. rgb = thisMainTrial.rgb)
    if thisMainTrial != None:
        for paramName in thisMainTrial:
            exec('{} = thisMainTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "experiment" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    stim1_main.setImage('../datasets/fmri_dataset/images/' + Stim1)
    stim2_main.setImage('../datasets/fmri_dataset/images/' + Stim2)
    stim3_main.setImage('../datasets/fmri_dataset/images/' + Stim3)
    # setup some python lists for storing info about the mouse_main
    mouse_main.x = []
    mouse_main.y = []
    mouse_main.leftButton = []
    mouse_main.midButton = []
    mouse_main.rightButton = []
    mouse_main.time = []
    mouse_main.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    experimentComponents = [fixation_main, frame1_main, frame2_main, frame3_main, stim1_main, stim2_main, stim3_main, mouse_main, question_text_2]
    for thisComponent in experimentComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "experiment" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_main* updates
        if fixation_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_main.frameNStart = frameN  # exact frame index
            fixation_main.tStart = t  # local t and not account for scr refresh
            fixation_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_main, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_main.started')
            fixation_main.setAutoDraw(True)
        if fixation_main.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_main.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_main.tStop = t  # not accounting for scr refresh
                fixation_main.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_main.stopped')
                fixation_main.setAutoDraw(False)
        
        # *frame1_main* updates
        if frame1_main.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            frame1_main.frameNStart = frameN  # exact frame index
            frame1_main.tStart = t  # local t and not account for scr refresh
            frame1_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(frame1_main, 'tStartRefresh')  # time at next scr refresh
            frame1_main.setAutoDraw(True)
        if frame1_main.status == STARTED:  # only update if drawing
            frame1_main.setOpacity(None, log=False)
        
        # *frame2_main* updates
        if frame2_main.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            frame2_main.frameNStart = frameN  # exact frame index
            frame2_main.tStart = t  # local t and not account for scr refresh
            frame2_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(frame2_main, 'tStartRefresh')  # time at next scr refresh
            frame2_main.setAutoDraw(True)
        if frame2_main.status == STARTED:  # only update if drawing
            frame2_main.setOpacity(None, log=False)
        
        # *frame3_main* updates
        if frame3_main.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            frame3_main.frameNStart = frameN  # exact frame index
            frame3_main.tStart = t  # local t and not account for scr refresh
            frame3_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(frame3_main, 'tStartRefresh')  # time at next scr refresh
            frame3_main.setAutoDraw(True)
        if frame3_main.status == STARTED:  # only update if drawing
            frame3_main.setOpacity(None, log=False)
        
        # *stim1_main* updates
        if stim1_main.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stim1_main.frameNStart = frameN  # exact frame index
            stim1_main.tStart = t  # local t and not account for scr refresh
            stim1_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim1_main, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stim1_main.started')
            stim1_main.setAutoDraw(True)
        
        # *stim2_main* updates
        if stim2_main.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stim2_main.frameNStart = frameN  # exact frame index
            stim2_main.tStart = t  # local t and not account for scr refresh
            stim2_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim2_main, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stim2_main.started')
            stim2_main.setAutoDraw(True)
        
        # *stim3_main* updates
        if stim3_main.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stim3_main.frameNStart = frameN  # exact frame index
            stim3_main.tStart = t  # local t and not account for scr refresh
            stim3_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim3_main, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stim3_main.started')
            stim3_main.setAutoDraw(True)
        # *mouse_main* updates
        if mouse_main.status == NOT_STARTED and t >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            mouse_main.frameNStart = frameN  # exact frame index
            mouse_main.tStart = t  # local t and not account for scr refresh
            mouse_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_main, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_main.started', t)
            mouse_main.status = STARTED
            mouse_main.mouseClock.reset()
            prevButtonState = mouse_main.getPressed()  # if button is down already this ISN'T a new click
        if mouse_main.status == STARTED:  # only update if started and not finished!
            buttons = mouse_main.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([stim1_main, stim2_main, stim3_main])
                        clickableList = [stim1_main, stim2_main, stim3_main]
                    except:
                        clickableList = [[stim1_main, stim2_main, stim3_main]]
                    for obj in clickableList:
                        if obj.contains(mouse_main):
                            gotValidClick = True
                            mouse_main.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = mouse_main.getPos()
                        mouse_main.x.append(x)
                        mouse_main.y.append(y)
                        buttons = mouse_main.getPressed()
                        mouse_main.leftButton.append(buttons[0])
                        mouse_main.midButton.append(buttons[1])
                        mouse_main.rightButton.append(buttons[2])
                        mouse_main.time.append(mouse_main.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *question_text_2* updates
        if question_text_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            question_text_2.frameNStart = frameN  # exact frame index
            question_text_2.tStart = t  # local t and not account for scr refresh
            question_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_text_2, 'tStartRefresh')  # time at next scr refresh
            question_text_2.setAutoDraw(True)
        # Run 'Each Frame' code from code_main
        # Get mouse position
        mouseX, mouseY = mouse_main.getPos()
        
        if stim1_main.contains(mouseX, mouseY):
            frame1_main.opacity = 1
        else:
            frame1_main.opacity = 0
            
        if stim2_main.contains(mouseX, mouseY):
            frame2_main.opacity = 1
        else:
            frame2_main.opacity = 0
            
        if stim3_main.contains(mouseX, mouseY):
            frame3_main.opacity = 1
        else:
            frame3_main.opacity = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in experimentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "experiment" ---
    for thisComponent in experimentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for mainTrials (TrialHandler)
    mainTrials.addData('mouse_main.x', mouse_main.x)
    mainTrials.addData('mouse_main.y', mouse_main.y)
    mainTrials.addData('mouse_main.leftButton', mouse_main.leftButton)
    mainTrials.addData('mouse_main.midButton', mouse_main.midButton)
    mainTrials.addData('mouse_main.rightButton', mouse_main.rightButton)
    mainTrials.addData('mouse_main.time', mouse_main.time)
    mainTrials.addData('mouse_main.clicked_name', mouse_main.clicked_name)
    # the Routine "experiment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'mainTrials'

# get names of stimulus parameters
if mainTrials.trialList in ([], [None], None):
    params = []
else:
    params = mainTrials.trialList[0].keys()
# save data for this loop
mainTrials.saveAsText(filename + 'mainTrials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "exit" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
exitComponents = [text_exit, key_resp_2]
for thisComponent in exitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "exit" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_exit* updates
    if text_exit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_exit.frameNStart = frameN  # exact frame index
        text_exit.tStart = t  # local t and not account for scr refresh
        text_exit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_exit, 'tStartRefresh')  # time at next scr refresh
        text_exit.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "exit" ---
for thisComponent in exitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "exit" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
