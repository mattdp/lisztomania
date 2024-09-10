#!/usr/bin/env python3

# import Task from parent folder in replicable way
import sys, os, random
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from task import Task

MORNING_WORK_RITUAL = [
    "DEPTH_DEFAULT",
    Task(title="Morning work routine",tags=["work"]),
    "DEPTH_DOWN",
    Task(title="Focus"),
    "DEPTH_DOWN",
    Task(title="Place nonessential devices in another room"),
    Task(title="Start a freedom session until the first long break"),
    Task(title="Set up some early Focusmates to make a solid start to the day"),
    "DEPTH_UP",
    Task(title="Exhortations"),
    "DEPTH_DOWN",
    Task(title="Focus"),
    "DEPTH_DOWN",
    Task(title="To achieve broader goals around being curious and living life well, you need to efficiently trade a limited amount of your time for a high amount of money."),
    Task(title="Rigorously prioritize which deals matter and hold yourself to a high standard on those deals. Qualify out mediocre deals rather than nurse them along"),
    Task(title="'Turn on' work and operate intensely when working, and 'turn off' work and don't let it dominate your mind when not working."),
    "DEPTH_UP",
    Task(title="Other reps don't matter to my happiness"),
    "DEPTH_DOWN",
    Task(title="Doesn't matter if others get advantages you don't, ultimately it's me vs. the golf course."),
    Task(title="Am I happy with my compensation and day to day work, even if others have advantages I consider unfair?"),
    Task(title="Will I be getting unfair advantages in the future outweighing the current annoyances?"),
    "DEPTH_UP",
    Task(title="Life is more important than work"),
    "DEPTH_DOWN",
    Task(title="For most of your work life, you've radiated stress at your loved ones."),
    Task(title="Focus on eating well, exercising, and low stress more than urgent job duties."),
    Task(title="You have many job options but one family and one body."),
    "DEPTH_UP",
    Task(title="Be positive"),
    "DEPTH_DOWN",
    Task(title="Whether this is stressful or fun is all mindset. If you're positive enough, clients and colleagues will root for you and make work and life easier."),
    "DEPTH_UP",
    Task(title="Achieve mastery"),
    "DEPTH_DOWN",
    Task(title="\"I'm not in the 0.1% of 'salespeople selling technical products to smart people' yet, but I will be someday. That's been my consistent goal since 2019.\""),
    Task(title="View every day as part of a 10+ year journey to master the craft. Passion comes and goes, but disciplined development of a skill that supports my family is an everyday task."),
    Task(title="Find at least 10 minutes to push outside your comfort zone and improve."),
    Task(title="If you don't learn, you get sad."),
    "DEPTH_UP",
    Task(title="When struggling to work well, consider"),
    "DEPTH_DOWN",
    Task(title="Is this a time I should be thinking strategically, or just doing? If just doing, do!!"),
    Task(title="If strategic, pick something important, and do singlemindedly for at least 20 minutes."),
    "DEPTH_UP",
    Task(title="Keep commitments to yourself"),
    "DEPTH_DOWN",
    Task(title="A giant ominous todo list causes you stress for no benefit. Be clear in the systems you build what needs to get done quickly, and keep that commitment."),
    Task(title="Hide what's unimportant and keep it out of your day-to-day thinking."),
    "DEPTH_UP",  
    Task(title="Network across a 10+ year period"),
    "DEPTH_DOWN",
    Task(title="Most of sales isn't hard. As AI improves, more of your value will be in who you know."),            
    Task(title="Spending time talking to people you genuninely like is a lot more fun than cold calling."),
    "DEPTH_UP", 
    "DEPTH_UP", 
    Task(title="Triage"),
    "DEPTH_DOWN",
    Task(title="Email triage: categorize to inbox 0"),
    Task(title="Slack triage: <=3m answer, else capture in GTD"),
    Task(title="Calendar check: any meetings today not prepped? When prepping?"),
    "DEPTH_UP",         
    Task(title="Key items: tag 2-3 most important work todos today", note= "Take a few moments to understand why you care about these things and what makes them important"),
    Task(title="Improvement: select what aiming to improve today with [#A] tag")
]

SALES_ROUTINE_TYPICAL = [
    "DEPTH_DEFAULT",
    Task(title="Daily workflow", tags=["work"]),
    "DEPTH_DOWN",        
    Task(title="Prep meetings that'll happen before deep work done"),
    Task(title="On call?"),
    "DEPTH_DOWN",        
    Task(title="If on call, turn on #livechat and respond to today's leads"),        
    Task(title="Hubspot Live Chats"),
    Task(title="Hubspot contact forms", note="https://app.hubspot.com/submissions/8863617/form/e194656e-6583-4896-a134-37e608428d0e/submissions/?redirectUrl=https%3A%2F%2Fapp.hubspot.com%2Fforms%2F8863617"),
    Task(title="sales@ emails"),
    "DEPTH_UP",           
    Task(title="Deep work on main goals for day"),
    Task(title="'1 few hours' email"),
    Task(title="Prep later meetings for today"),
    Task(title="Tier 0 GTD"),
    Task(title="SSS give 5 tacos and post my progress"),
    Task(title="15 minutes impactful prospecting"),
    Task(title="'2 within BD' email"),
    Task(title="Tier 1 GTD"),
    Task(title="Full pomodoro of personal or sales learning", note="https://keep.google.com/"),
    Task(title="Email remind people of convos in 2 biz days, if not a recent booking"),
    Task(title="Prep tomorrow's meetings"),
    Task(title="Full pomodoro of personal admin/todos", note="https://keep.google.com/"),
    Task(title="15 more minutes prospecting"),
    Task(title="Tier 2 GTD"),
    Task(title="Prep tomorrow's meetings"),
    Task(title="Prospect at least 1 hour"),
    Task(title="Tier 3 + 4 GTD")
]

always_start = [
    "DEPTH_DEFAULT",
    Task(title="Daily workflow", tags=["work"]),
    "DEPTH_DOWN",        
    Task(title="Prep meetings that'll happen before deep work done"),
    Task(title="On call?"),
    "DEPTH_DOWN",        
    Task(title="If on call, turn on #livechat and respond to today's leads"),        
    Task(title="Hubspot Live Chats"),
    Task(title="Hubspot contact forms", note="https://app.hubspot.com/submissions/8863617/form/e194656e-6583-4896-a134-37e608428d0e/submissions/?redirectUrl=https%3A%2F%2Fapp.hubspot.com%2Fforms%2F8863617"),
    Task(title="sales@ emails"),
    "DEPTH_UP"
]    

arbitrary_order = [
    Task(title="Deep work on main goals for day"),
    Task(title="'1 few hours' email"),
    Task(title="Prep later meetings for today"),
    Task(title="Tier 0 GTD"),
    Task(title="SSS give 5 tacos and post my progress"),
    Task(title="15 minutes impactful prospecting"),
    Task(title="'2 within BD' email"),
    Task(title="Tier 1 GTD"),
    Task(title="Full pomodoro of personal or sales learning", note="https://keep.google.com/"),
    Task(title="Email remind people of convos in 2 biz days, if not a recent booking"),
]
if random.randint(1,10) >= 6:
    arbitrary_order += [Task(title="Go do something fun for 15 minutes!")]

random.shuffle(arbitrary_order)

closing = [
    Task(title="Prep tomorrow's meetings"),
    Task(title="Full pomodoro of personal admin/todos", note="https://keep.google.com/"),
    Task(title="15 more minutes prospecting"),
    Task(title="Tier 2 GTD"),
    Task(title="Prep tomorrow's meetings"),
    Task(title="Prospect at least 1 hour"),
    Task(title="Tier 3 + 4 GTD")
]

class Instructions:

    def instructions_list():
        instructions = MORNING_WORK_RITUAL + always_start + arbitrary_order + closing
        return instructions