/******************************* 
 * Odd_One_Out_Experiment Test *
 *******************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.5.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'odd_one_out_experiment';  // from the Builder filename that created this script
let expInfo = {
    'participant': '000',
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from code
let nPractice = 5;
let nMain = 50;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(exampleRoutineBegin());
flowScheduler.add(exampleRoutineEachFrame());
flowScheduler.add(exampleRoutineEnd());
const practiceTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceTrialsLoopBegin(practiceTrialsLoopScheduler));
flowScheduler.add(practiceTrialsLoopScheduler);
flowScheduler.add(practiceTrialsLoopEnd);
flowScheduler.add(pauseRoutineBegin());
flowScheduler.add(pauseRoutineEachFrame());
flowScheduler.add(pauseRoutineEnd());
const mainTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(mainTrialsLoopBegin(mainTrialsLoopScheduler));
flowScheduler.add(mainTrialsLoopScheduler);
flowScheduler.add(mainTrialsLoopEnd);
flowScheduler.add(exitRoutineBegin());
flowScheduler.add(exitRoutineEachFrame());
flowScheduler.add(exitRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'datasets/fmri_dataset/images/C1_Images_WinterFriede(Reversed).png', 'path': 'datasets/fmri_dataset/images/C1_Images_WinterFriede(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/NC2_Images_KekhayovPetrov(Nomate)(Reversed).png', 'path': 'datasets/fmri_dataset/images/NC2_Images_KekhayovPetrov(Nomate)(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/NC3_Images_KazicVukovic(Nomate)(Reversed).png', 'path': 'datasets/fmri_dataset/images/NC3_Images_KazicVukovic(Nomate)(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/NC2_Images_Replacement4(Nomate).png', 'path': 'datasets/fmri_dataset/images/NC2_Images_Replacement4(Nomate).png'},
    {'name': 'datasets/fmri_dataset/images/C5_Images_EasyPosition6.png', 'path': 'datasets/fmri_dataset/images/C5_Images_EasyPosition6.png'},
    {'name': 'datasets/fmri_dataset/images/C2_Images_KekhayovPetrov(Reversed).png', 'path': 'datasets/fmri_dataset/images/C2_Images_KekhayovPetrov(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/NC4_Images_StrekalovskyShaposhlikov(Nomate).png', 'path': 'datasets/fmri_dataset/images/NC4_Images_StrekalovskyShaposhlikov(Nomate).png'},
    {'name': 'datasets/fmri_dataset/images/C2_Images_SkujaRozenbergs(Reversed).png', 'path': 'datasets/fmri_dataset/images/C2_Images_SkujaRozenbergs(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/C3_Images_PodzerovKuntzevic(Reversed).png', 'path': 'datasets/fmri_dataset/images/C3_Images_PodzerovKuntzevic(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/NC2_Images_SkujaRozenbergs(Nomate)(Reversed).png', 'path': 'datasets/fmri_dataset/images/NC2_Images_SkujaRozenbergs(Nomate)(Reversed).png'},
    {'name': 'instructFrame1.png', 'path': 'instructFrame1.png'},
    {'name': 'datasets/fmri_dataset/images/NC3_Images_StudybyErcoleDelRio(Nomate)(Reversed).png', 'path': 'datasets/fmri_dataset/images/NC3_Images_StudybyErcoleDelRio(Nomate)(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/NC3_Images_Replacement5(Nomate).png', 'path': 'datasets/fmri_dataset/images/NC3_Images_Replacement5(Nomate).png'},
    {'name': 'datasets/fmri_dataset/images/NC3_Images_Replacement3(Nomate).png', 'path': 'datasets/fmri_dataset/images/NC3_Images_Replacement3(Nomate).png'},
    {'name': 'datasets/fmri_dataset/images/C3_Images_Replacement3.png', 'path': 'datasets/fmri_dataset/images/C3_Images_Replacement3.png'},
    {'name': 'datasets/fmri_dataset/images/NC4_Images_BrankaWittwer(Nomate)(Reversed).png', 'path': 'datasets/fmri_dataset/images/NC4_Images_BrankaWittwer(Nomate)(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/C3_Images_MalininAndreev(Reversed).png', 'path': 'datasets/fmri_dataset/images/C3_Images_MalininAndreev(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/NC1_Images_WinterFriede(Nomate)(Reversed).png', 'path': 'datasets/fmri_dataset/images/NC1_Images_WinterFriede(Nomate)(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/NC2_Images_KrauseMeinhardt(Nomate).png', 'path': 'datasets/fmri_dataset/images/NC2_Images_KrauseMeinhardt(Nomate).png'},
    {'name': 'datasets/fmri_dataset/images/C2_Images_Replacement4.png', 'path': 'datasets/fmri_dataset/images/C2_Images_Replacement4.png'},
    {'name': 'datasets/fmri_dataset/images/NC3_Images_TylorWinter(Nomate).png', 'path': 'datasets/fmri_dataset/images/NC3_Images_TylorWinter(Nomate).png'},
    {'name': 'datasets/fmri_dataset/images/C1_Images_Frombeautiful.png', 'path': 'datasets/fmri_dataset/images/C1_Images_Frombeautiful.png'},
    {'name': 'datasets/fmri_dataset/images/C3_Images_TylorWinter.png', 'path': 'datasets/fmri_dataset/images/C3_Images_TylorWinter.png'},
    {'name': 'datasets/fmri_dataset/images/C3_Images_KazicVukovic(Reversed).png', 'path': 'datasets/fmri_dataset/images/C3_Images_KazicVukovic(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/NC5_Images_EasyPosition2(Nomate).png', 'path': 'datasets/fmri_dataset/images/NC5_Images_EasyPosition2(Nomate).png'},
    {'name': 'dataset.csv', 'path': 'dataset.csv'},
    {'name': 'datasets/fmri_dataset/images/C5_Images_EasyPosition2.png', 'path': 'datasets/fmri_dataset/images/C5_Images_EasyPosition2.png'},
    {'name': 'datasets/fmri_dataset/images/NC1_Images_SteinitzNN(Nomate).png', 'path': 'datasets/fmri_dataset/images/NC1_Images_SteinitzNN(Nomate).png'},
    {'name': 'datasets/fmri_dataset/images/C2_Images_KrauseMeinhardt.png', 'path': 'datasets/fmri_dataset/images/C2_Images_KrauseMeinhardt.png'},
    {'name': 'datasets/fmri_dataset/images/C5_Images_EasyPosition5(Reversed).png', 'path': 'datasets/fmri_dataset/images/C5_Images_EasyPosition5(Reversed).png'},
    {'name': 'triplets.csv', 'path': 'triplets.csv'},
    {'name': 'datasets/fmri_dataset/images/C4_Images_IvanchukSavchenko(Reversed).png', 'path': 'datasets/fmri_dataset/images/C4_Images_IvanchukSavchenko(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/NC3_Images_PodzerovKuntzevic(Nomate)(Reversed).png', 'path': 'datasets/fmri_dataset/images/NC3_Images_PodzerovKuntzevic(Nomate)(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/C3_Images_Replacement5.png', 'path': 'datasets/fmri_dataset/images/C3_Images_Replacement5.png'},
    {'name': 'datasets/fmri_dataset/images/NC5_Images_EasyPosition5(Nomate)(Reversed).png', 'path': 'datasets/fmri_dataset/images/NC5_Images_EasyPosition5(Nomate)(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/C3_Images_StudybyErcoledelRio(Reversed).png', 'path': 'datasets/fmri_dataset/images/C3_Images_StudybyErcoledelRio(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/NC5_Images_EasyPosition6(Nomate).png', 'path': 'datasets/fmri_dataset/images/NC5_Images_EasyPosition6(Nomate).png'},
    {'name': 'datasets/fmri_dataset/images/C4_Images_BrankaWittwer(Reversed).png', 'path': 'datasets/fmri_dataset/images/C4_Images_BrankaWittwer(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/C4_Images_StrekalovskyShaposhlikov.png', 'path': 'datasets/fmri_dataset/images/C4_Images_StrekalovskyShaposhlikov.png'},
    {'name': 'datasets/fmri_dataset/images/NC4_Images_IvanchukSavchenko(Nomate)(Reversed).png', 'path': 'datasets/fmri_dataset/images/NC4_Images_IvanchukSavchenko(Nomate)(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/NC3_Images_MalininAndreev(Nomate)(Reversed).png', 'path': 'datasets/fmri_dataset/images/NC3_Images_MalininAndreev(Nomate)(Reversed).png'},
    {'name': 'datasets/fmri_dataset/images/C1_Images_SteinitzNN.png', 'path': 'datasets/fmri_dataset/images/C1_Images_SteinitzNN.png'},
    {'name': 'datasets/fmri_dataset/images/NC1_Images_Frombeautiful(Nomate).png', 'path': 'datasets/fmri_dataset/images/NC1_Images_Frombeautiful(Nomate).png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.5';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + ((("data/" + "sub_") + expInfo["participant"]) + `/sub${expInfo["participant"]}_run${expInfo["session"]}_${expName}_${expInfo["date"]}`));


  return Scheduler.Event.NEXT;
}


var welcomeClock;
var welcomeText;
var key_resp;
var exampleClock;
var instr_image;
var text;
var key_example;
var practiceClock;
var fixation_practice;
var frame1;
var frame2;
var frame3;
var stim1_pract;
var stim2_pract;
var stim3_pract;
var mouse_pract;
var question_text;
var pauseClock;
var pauseText;
var key_resp_pause;
var experimentClock;
var fixation_main;
var frame1_main;
var frame2_main;
var frame3_main;
var stim1_main;
var stim2_main;
var stim3_main;
var mouse_main;
var question_text_2;
var exitClock;
var text_exit;
var key_resp_2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  welcomeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcomeText',
    text: "Welcome, in this experiment you will be presented with three chess scenario's, side-by-side.\n\nIt is your task to select the odd-one-out. In other words, choose the one you think is the most different when comparing to the other two scenario's.\n\nTo select the odd-one-out you can use your mouse. Click on the scenario you think is the most distinct. \n\nWe will first show you an example of a single trial. It is not necessary to pay attention to the correctness of the decision, rather focus on the general lay-out of the task.\n\nAfter the example you can practice the task yourself.\n\nPress <space> to continue...",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "example"
  exampleClock = new util.Clock();
  instr_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instr_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.7, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 256.0, interpolate : true, depth : 0.0 
  });
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: "Let's say you think the most distinct scenario is the one in the middle.\nYou can then use your mouse to select this specific scenario as the odd-one-out. \n\nPress <space> to continue to the practice trials...",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.35)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_example = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice"
  practiceClock = new util.Clock();
  fixation_practice = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_practice', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  frame1 = new visual.Rect ({
    win: psychoJS.window, name: 'frame1', 
    width: [0.45, 0.45][0], height: [0.45, 0.45][1],
    ori: 0.0, pos: [(- 0.5), 0],
    lineWidth: 2.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.0, 0.0, 0.0]),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  frame2 = new visual.Rect ({
    win: psychoJS.window, name: 'frame2', 
    width: [0.45, 0.45][0], height: [0.45, 0.45][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 2.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.0, 0.0, 0.0]),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  frame3 = new visual.Rect ({
    win: psychoJS.window, name: 'frame3', 
    width: [0.45, 0.45][0], height: [0.45, 0.45][1],
    ori: 0.0, pos: [0.5, 0],
    lineWidth: 2.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.0, 0.0, 0.0]),
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  stim1_pract = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stim1_pract', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.5), 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  stim2_pract = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stim2_pract', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  stim3_pract = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stim3_pract', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.5, 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  mouse_pract = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_pract.mouseClock = new util.Clock();
  question_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_text',
    text: 'Which is the odd-one-out?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  // Initialize components for Routine "pause"
  pauseClock = new util.Clock();
  pauseText = new visual.TextStim({
    win: psychoJS.window,
    name: 'pauseText',
    text: "We have finished practicing!\n\nLet's start with the experiment, the task remains the same as it was during practice.\n\nPress <space> to continue...",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_pause = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "experiment"
  experimentClock = new util.Clock();
  fixation_main = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_main', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  frame1_main = new visual.Rect ({
    win: psychoJS.window, name: 'frame1_main', 
    width: [0.45, 0.45][0], height: [0.45, 0.45][1],
    ori: 0.0, pos: [(- 0.5), 0],
    lineWidth: 2.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.0, 0.0, 0.0]),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  frame2_main = new visual.Rect ({
    win: psychoJS.window, name: 'frame2_main', 
    width: [0.45, 0.45][0], height: [0.45, 0.45][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 2.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.0, 0.0, 0.0]),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  frame3_main = new visual.Rect ({
    win: psychoJS.window, name: 'frame3_main', 
    width: [0.45, 0.45][0], height: [0.45, 0.45][1],
    ori: 0.0, pos: [0.5, 0],
    lineWidth: 2.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.0, 0.0, 0.0]),
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  stim1_main = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stim1_main', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.5), 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  stim2_main = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stim2_main', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  stim3_main = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stim3_main', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.5, 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  mouse_main = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_main.mouseClock = new util.Clock();
  question_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_text_2',
    text: 'Which is the odd-one-out?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  // Initialize components for Routine "exit"
  exitClock = new util.Clock();
  text_exit = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_exit',
    text: 'That was it!\n\nThank you for your time and attention.\n\nPress <space> to leave the experiment.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_allKeys;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcome' ---
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(welcomeText);
    welcomeComponents.push(key_resp);
    
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcome' ---
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcomeText* updates
    if (t >= 0.0 && welcomeText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcomeText.tStart = t;  // (not accounting for frame time here)
      welcomeText.frameNStart = frameN;  // exact frame index
      
      welcomeText.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 1 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcome' ---
    for (const thisComponent of welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_example_allKeys;
var exampleComponents;
function exampleRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'example' ---
    t = 0;
    exampleClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_example.keys = undefined;
    key_example.rt = undefined;
    _key_example_allKeys = [];
    // keep track of which components have finished
    exampleComponents = [];
    exampleComponents.push(instr_image);
    exampleComponents.push(text);
    exampleComponents.push(key_example);
    
    for (const thisComponent of exampleComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function exampleRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'example' ---
    // get current time
    t = exampleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_image* updates
    if (t >= 0 && instr_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_image.tStart = t;  // (not accounting for frame time here)
      instr_image.frameNStart = frameN;  // exact frame index
      
      instr_image.setAutoDraw(true);
    }

    
    if (instr_image.status === PsychoJS.Status.STARTED){ // only update if being drawn
      instr_image.setImage('instructFrame1.png', false);
    }
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_example* updates
    if (t >= 0.0 && key_example.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_example.tStart = t;  // (not accounting for frame time here)
      key_example.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_example.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_example.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_example.clearEvents(); });
    }

    if (key_example.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_example.getKeys({keyList: ['space'], waitRelease: false});
      _key_example_allKeys = _key_example_allKeys.concat(theseKeys);
      if (_key_example_allKeys.length > 0) {
        key_example.keys = _key_example_allKeys[_key_example_allKeys.length - 1].name;  // just the last key pressed
        key_example.rt = _key_example_allKeys[_key_example_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of exampleComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function exampleRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'example' ---
    for (const thisComponent of exampleComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_example.corr, level);
    }
    psychoJS.experiment.addData('key_example.keys', key_example.keys);
    if (typeof key_example.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_example.rt', key_example.rt);
        routineTimer.reset();
        }
    
    key_example.stop();
    // the Routine "example" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practiceTrials;
function practiceTrialsLoopBegin(practiceTrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practiceTrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'triplets.csv',
      seed: undefined, name: 'practiceTrials'
    });
    psychoJS.experiment.addLoop(practiceTrials); // add the loop to the experiment
    currentLoop = practiceTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPracticeTrial of practiceTrials) {
      snapshot = practiceTrials.getSnapshot();
      practiceTrialsLoopScheduler.add(importConditions(snapshot));
      practiceTrialsLoopScheduler.add(practiceRoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(practiceRoutineEachFrame());
      practiceTrialsLoopScheduler.add(practiceRoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(practiceTrialsLoopEndIteration(practiceTrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function practiceTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practiceTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practiceTrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var mainTrials;
function mainTrialsLoopBegin(mainTrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    mainTrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'triplets.csv',
      seed: undefined, name: 'mainTrials'
    });
    psychoJS.experiment.addLoop(mainTrials); // add the loop to the experiment
    currentLoop = mainTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisMainTrial of mainTrials) {
      snapshot = mainTrials.getSnapshot();
      mainTrialsLoopScheduler.add(importConditions(snapshot));
      mainTrialsLoopScheduler.add(experimentRoutineBegin(snapshot));
      mainTrialsLoopScheduler.add(experimentRoutineEachFrame());
      mainTrialsLoopScheduler.add(experimentRoutineEnd(snapshot));
      mainTrialsLoopScheduler.add(mainTrialsLoopEndIteration(mainTrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function mainTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(mainTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function mainTrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var gotValidClick;
var practiceComponents;
function practiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice' ---
    t = 0;
    practiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    stim1_pract.setImage(("datasets/fmri_dataset/images/" + Stim1));
    stim2_pract.setImage(("datasets/fmri_dataset/images/" + Stim2));
    stim3_pract.setImage(("datasets/fmri_dataset/images/" + Stim3));
    // setup some python lists for storing info about the mouse_pract
    // current position of the mouse:
    mouse_pract.x = [];
    mouse_pract.y = [];
    mouse_pract.leftButton = [];
    mouse_pract.midButton = [];
    mouse_pract.rightButton = [];
    mouse_pract.time = [];
    mouse_pract.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    practiceComponents = [];
    practiceComponents.push(fixation_practice);
    practiceComponents.push(frame1);
    practiceComponents.push(frame2);
    practiceComponents.push(frame3);
    practiceComponents.push(stim1_pract);
    practiceComponents.push(stim2_pract);
    practiceComponents.push(stim3_pract);
    practiceComponents.push(mouse_pract);
    practiceComponents.push(question_text);
    
    for (const thisComponent of practiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function practiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice' ---
    // get current time
    t = practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_practice* updates
    if (t >= 0.0 && fixation_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_practice.tStart = t;  // (not accounting for frame time here)
      fixation_practice.frameNStart = frameN;  // exact frame index
      
      fixation_practice.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_practice.setAutoDraw(false);
    }
    
    // *frame1* updates
    if (t >= 0.5 && frame1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      frame1.tStart = t;  // (not accounting for frame time here)
      frame1.frameNStart = frameN;  // exact frame index
      
      frame1.setAutoDraw(true);
    }

    
    if (frame1.status === PsychoJS.Status.STARTED){ // only update if being drawn
      frame1.setOpacity(None, false);
    }
    
    // *frame2* updates
    if (t >= 0.5 && frame2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      frame2.tStart = t;  // (not accounting for frame time here)
      frame2.frameNStart = frameN;  // exact frame index
      
      frame2.setAutoDraw(true);
    }

    
    if (frame2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      frame2.setOpacity(None, false);
    }
    
    // *frame3* updates
    if (t >= 0.5 && frame3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      frame3.tStart = t;  // (not accounting for frame time here)
      frame3.frameNStart = frameN;  // exact frame index
      
      frame3.setAutoDraw(true);
    }

    
    if (frame3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      frame3.setOpacity(None, false);
    }
    
    // *stim1_pract* updates
    if (t >= 0.5 && stim1_pract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim1_pract.tStart = t;  // (not accounting for frame time here)
      stim1_pract.frameNStart = frameN;  // exact frame index
      
      stim1_pract.setAutoDraw(true);
    }

    
    // *stim2_pract* updates
    if (t >= 0.5 && stim2_pract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim2_pract.tStart = t;  // (not accounting for frame time here)
      stim2_pract.frameNStart = frameN;  // exact frame index
      
      stim2_pract.setAutoDraw(true);
    }

    
    // *stim3_pract* updates
    if (t >= 0.5 && stim3_pract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim3_pract.tStart = t;  // (not accounting for frame time here)
      stim3_pract.frameNStart = frameN;  // exact frame index
      
      stim3_pract.setAutoDraw(true);
    }

    // *mouse_pract* updates
    if (t >= 0.5 && mouse_pract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_pract.tStart = t;  // (not accounting for frame time here)
      mouse_pract.frameNStart = frameN;  // exact frame index
      
      mouse_pract.status = PsychoJS.Status.STARTED;
      mouse_pract.mouseClock.reset();
      prevButtonState = mouse_pract.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_pract.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_pract.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [stim1_pract, stim2_pract, stim3_pract]) {
            if (obj.contains(mouse_pract)) {
              gotValidClick = true;
              mouse_pract.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouse_pract.getPos();
            mouse_pract.x.push(_mouseXYs[0]);
            mouse_pract.y.push(_mouseXYs[1]);
            mouse_pract.leftButton.push(_mouseButtons[0]);
            mouse_pract.midButton.push(_mouseButtons[1]);
            mouse_pract.rightButton.push(_mouseButtons[2]);
            mouse_pract.time.push(mouse_pract.mouseClock.getTime());
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *question_text* updates
    if (t >= 0.5 && question_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_text.tStart = t;  // (not accounting for frame time here)
      question_text.frameNStart = frameN;  // exact frame index
      
      question_text.setAutoDraw(true);
    }

    // Run 'Each Frame' code from code_pract
    let [mouseX, mouseY] = mouse_pract.getPos();
    if (stim1_pract.contains(mouseX, mouseY)) {
        frame1.opacity = 1;
    } else {
        frame1.opacity = 0;
    }
    if (stim2_pract.contains(mouseX, mouseY)) {
        frame2.opacity = 1;
    } else {
        frame2.opacity = 0;
    }
    if (stim3_pract.contains(mouseX, mouseY)) {
        frame3.opacity = 1;
    } else {
        frame3.opacity = 0;
    }
    if ((practiceTrials.thisN === (nPractice - 1))) {
        practiceTrials.finished = true;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice' ---
    for (const thisComponent of practiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_pract.x) {  psychoJS.experiment.addData('mouse_pract.x', mouse_pract.x[0])};
    if (mouse_pract.y) {  psychoJS.experiment.addData('mouse_pract.y', mouse_pract.y[0])};
    if (mouse_pract.leftButton) {  psychoJS.experiment.addData('mouse_pract.leftButton', mouse_pract.leftButton[0])};
    if (mouse_pract.midButton) {  psychoJS.experiment.addData('mouse_pract.midButton', mouse_pract.midButton[0])};
    if (mouse_pract.rightButton) {  psychoJS.experiment.addData('mouse_pract.rightButton', mouse_pract.rightButton[0])};
    if (mouse_pract.time) {  psychoJS.experiment.addData('mouse_pract.time', mouse_pract.time[0])};
    if (mouse_pract.clicked_name) {  psychoJS.experiment.addData('mouse_pract.clicked_name', mouse_pract.clicked_name[0])};
    
    // the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_pause_allKeys;
var pauseComponents;
function pauseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pause' ---
    t = 0;
    pauseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_pause.keys = undefined;
    key_resp_pause.rt = undefined;
    _key_resp_pause_allKeys = [];
    // keep track of which components have finished
    pauseComponents = [];
    pauseComponents.push(pauseText);
    pauseComponents.push(key_resp_pause);
    
    for (const thisComponent of pauseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function pauseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pause' ---
    // get current time
    t = pauseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pauseText* updates
    if (t >= 0.0 && pauseText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pauseText.tStart = t;  // (not accounting for frame time here)
      pauseText.frameNStart = frameN;  // exact frame index
      
      pauseText.setAutoDraw(true);
    }

    
    // *key_resp_pause* updates
    if (t >= 0.0 && key_resp_pause.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_pause.tStart = t;  // (not accounting for frame time here)
      key_resp_pause.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_pause.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_pause.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_pause.clearEvents(); });
    }

    if (key_resp_pause.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_pause.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_pause_allKeys = _key_resp_pause_allKeys.concat(theseKeys);
      if (_key_resp_pause_allKeys.length > 0) {
        key_resp_pause.keys = _key_resp_pause_allKeys[_key_resp_pause_allKeys.length - 1].name;  // just the last key pressed
        key_resp_pause.rt = _key_resp_pause_allKeys[_key_resp_pause_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of pauseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pauseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pause' ---
    for (const thisComponent of pauseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_pause.stop();
    // the Routine "pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var experimentComponents;
function experimentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'experiment' ---
    t = 0;
    experimentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    stim1_main.setImage(("datasets/fmri_dataset/images/" + Stim1));
    stim2_main.setImage(("datasets/fmri_dataset/images/" + Stim2));
    stim3_main.setImage(("datasets/fmri_dataset/images/" + Stim3));
    // setup some python lists for storing info about the mouse_main
    // current position of the mouse:
    mouse_main.x = [];
    mouse_main.y = [];
    mouse_main.leftButton = [];
    mouse_main.midButton = [];
    mouse_main.rightButton = [];
    mouse_main.time = [];
    mouse_main.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    experimentComponents = [];
    experimentComponents.push(fixation_main);
    experimentComponents.push(frame1_main);
    experimentComponents.push(frame2_main);
    experimentComponents.push(frame3_main);
    experimentComponents.push(stim1_main);
    experimentComponents.push(stim2_main);
    experimentComponents.push(stim3_main);
    experimentComponents.push(mouse_main);
    experimentComponents.push(question_text_2);
    
    for (const thisComponent of experimentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function experimentRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'experiment' ---
    // get current time
    t = experimentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_main* updates
    if (t >= 0.0 && fixation_main.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_main.tStart = t;  // (not accounting for frame time here)
      fixation_main.frameNStart = frameN;  // exact frame index
      
      fixation_main.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_main.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_main.setAutoDraw(false);
    }
    
    // *frame1_main* updates
    if (t >= 0.5 && frame1_main.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      frame1_main.tStart = t;  // (not accounting for frame time here)
      frame1_main.frameNStart = frameN;  // exact frame index
      
      frame1_main.setAutoDraw(true);
    }

    
    if (frame1_main.status === PsychoJS.Status.STARTED){ // only update if being drawn
      frame1_main.setOpacity(None, false);
    }
    
    // *frame2_main* updates
    if (t >= 0.5 && frame2_main.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      frame2_main.tStart = t;  // (not accounting for frame time here)
      frame2_main.frameNStart = frameN;  // exact frame index
      
      frame2_main.setAutoDraw(true);
    }

    
    if (frame2_main.status === PsychoJS.Status.STARTED){ // only update if being drawn
      frame2_main.setOpacity(None, false);
    }
    
    // *frame3_main* updates
    if (t >= 0.5 && frame3_main.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      frame3_main.tStart = t;  // (not accounting for frame time here)
      frame3_main.frameNStart = frameN;  // exact frame index
      
      frame3_main.setAutoDraw(true);
    }

    
    if (frame3_main.status === PsychoJS.Status.STARTED){ // only update if being drawn
      frame3_main.setOpacity(None, false);
    }
    
    // *stim1_main* updates
    if (t >= 0.5 && stim1_main.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim1_main.tStart = t;  // (not accounting for frame time here)
      stim1_main.frameNStart = frameN;  // exact frame index
      
      stim1_main.setAutoDraw(true);
    }

    
    // *stim2_main* updates
    if (t >= 0.5 && stim2_main.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim2_main.tStart = t;  // (not accounting for frame time here)
      stim2_main.frameNStart = frameN;  // exact frame index
      
      stim2_main.setAutoDraw(true);
    }

    
    // *stim3_main* updates
    if (t >= 0.5 && stim3_main.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim3_main.tStart = t;  // (not accounting for frame time here)
      stim3_main.frameNStart = frameN;  // exact frame index
      
      stim3_main.setAutoDraw(true);
    }

    // *mouse_main* updates
    if (t >= 0.5 && mouse_main.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_main.tStart = t;  // (not accounting for frame time here)
      mouse_main.frameNStart = frameN;  // exact frame index
      
      mouse_main.status = PsychoJS.Status.STARTED;
      mouse_main.mouseClock.reset();
      prevButtonState = mouse_main.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_main.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_main.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [stim1_main, stim2_main, stim3_main]) {
            if (obj.contains(mouse_main)) {
              gotValidClick = true;
              mouse_main.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouse_main.getPos();
            mouse_main.x.push(_mouseXYs[0]);
            mouse_main.y.push(_mouseXYs[1]);
            mouse_main.leftButton.push(_mouseButtons[0]);
            mouse_main.midButton.push(_mouseButtons[1]);
            mouse_main.rightButton.push(_mouseButtons[2]);
            mouse_main.time.push(mouse_main.mouseClock.getTime());
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *question_text_2* updates
    if (t >= 0.5 && question_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_text_2.tStart = t;  // (not accounting for frame time here)
      question_text_2.frameNStart = frameN;  // exact frame index
      
      question_text_2.setAutoDraw(true);
    }

    // Run 'Each Frame' code from code_main
    let [mouseX, mouseY] = mouse_main.getPos();
    if (stim1_main.contains(mouseX, mouseY)) {
        frame1_main.opacity = 1;
    } else {
        frame1_main.opacity = 0;
    }
    if (stim2_main.contains(mouseX, mouseY)) {
        frame2_main.opacity = 1;
    } else {
        frame2_main.opacity = 0;
    }
    if (stim3_main.contains(mouseX, mouseY)) {
        frame3_main.opacity = 1;
    } else {
        frame3_main.opacity = 0;
    }
    if ((mainTrials.thisN === (nMain - 1))) {
        mainTrials.finished = true;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of experimentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function experimentRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'experiment' ---
    for (const thisComponent of experimentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_main.x) {  psychoJS.experiment.addData('mouse_main.x', mouse_main.x[0])};
    if (mouse_main.y) {  psychoJS.experiment.addData('mouse_main.y', mouse_main.y[0])};
    if (mouse_main.leftButton) {  psychoJS.experiment.addData('mouse_main.leftButton', mouse_main.leftButton[0])};
    if (mouse_main.midButton) {  psychoJS.experiment.addData('mouse_main.midButton', mouse_main.midButton[0])};
    if (mouse_main.rightButton) {  psychoJS.experiment.addData('mouse_main.rightButton', mouse_main.rightButton[0])};
    if (mouse_main.time) {  psychoJS.experiment.addData('mouse_main.time', mouse_main.time[0])};
    if (mouse_main.clicked_name) {  psychoJS.experiment.addData('mouse_main.clicked_name', mouse_main.clicked_name[0])};
    
    // the Routine "experiment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_2_allKeys;
var exitComponents;
function exitRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'exit' ---
    t = 0;
    exitClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    exitComponents = [];
    exitComponents.push(text_exit);
    exitComponents.push(key_resp_2);
    
    for (const thisComponent of exitComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function exitRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'exit' ---
    // get current time
    t = exitClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_exit* updates
    if (t >= 0.0 && text_exit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_exit.tStart = t;  // (not accounting for frame time here)
      text_exit.frameNStart = frameN;  // exact frame index
      
      text_exit.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.5 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of exitComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function exitRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'exit' ---
    for (const thisComponent of exitComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "exit" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
