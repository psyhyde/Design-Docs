# UML Still Relevant ?

## Software Engineering 

Should you use UML?** It depends on the complexity and what you expect from UML.

Here's a totally non-scientific method, but I'll use it anyway: a search today for "Software Engineer" positions on a popular recruiting web site revealed more than 1000 in Silicon Valley. However, if you filter that search with the words "UML" in the offer, the market reduces to just 20 jobs! From the descriptions, they tend to be more senior positions. Conclusion: you won't need to learn UML to find a job. You might need it in a senior position at Amazon or Google Android (based on a few of the companies I saw in the offers).

**Is it useful if you care about code quality?** I think UML is going to help you improve your *design* at the modular (class) level or higher -- not because UML has some magic power, but because it helps you to abstract the important things at this level, leaving out the *tedious details* you'll find throughout the code. Models are about abstracting the essential.

UML class diagrams show easily how coupling is reduced in a design after applying a design pattern (which are usually documented with UML). I'd postulate it's going to be harder to use OO design patterns in a team if you don't know UML. But it's still only a model. "Bubbles don't crash" is a famous phrase from Bertrand Meyer, which means you'll still have to be good at coding your design. MDA/MDD isn't ready for most of the market yet.

**Is there any other lightweight software...?** UML as a whole is not lightweight, but you can use it in a lightweight manner. Whiteboard sketching is very lightweight and I find allows a different creativity than with my hand on the mouse looking at a screen. A couple of tools I like for doing lightweight UML are UMLet and PlantUML. The latter even has an add-on for Google Docs called PlantUML Gizmo (disclaimer - I am the developer, but it's free software I developed as a "community service" in my role as a university professor).

Here's an example of UML produced by PlantUML:

![img](https://qph.fs.quoracdn.net/main-qimg-c842a9fb02ba2fbed3a9df7577054761.webp)

You can view the source code at the [PlantUMLServer](http://www.plantuml.com/plantuml/form?url=JSun3eCm30NGcPpYNu0BC23HhSSmO4Y4SQeuhTJRrpH3AqKUxE_dJ98MxiTRdZ4WiaWEcYj3UAi3Qam6VuGj5QkuHi6Ef0ygTCBgMzXhIKjzdX9SwSVf4XtBHvDAskC_vSt8fL5jens_mqLFgVFxxnEXevRj5bAGMCRCM7bBocleiiBunOK4uXqBhEit_m40).

A couple of final comments:

- As another answer pointed out, the industry is craving many more concrete developers (who are manufacturing software as a *commodity*) than classically trained (?) software engineers (as we teach it at a university). The truth is, if a software company doesn't get some version 1.0 of their product out the door, it won't matter if the code is maintainable, well-designed, etc. Commoditization changes the game a lot, and software engineering education doesn't react that quickly to the trends (which isn't a bad thing necessarily, as some trends fade out). The standard for "competent" software engineers has lowered because the demand is high. This is not a reason to dismiss UML in my opinion. I go back to my job-search anecdote. Do you want to get a programming job just anywhere in Silicon Valley, or work for Google on the Android team?
- UML puts the abstractions into focus (which is good for design and architecture) but sometimes you have to "Just code it™" (because the devil is in the details). Many developers who learn to use UML have trouble switching back and forth, or balancing the attention they put at various levels. Working at various levels of abstraction is actually pretty hard. Spending too much energy on the abstractions (neglecting the code) won't help the company get out that version 1.0 (think "analysis paralysis"). You might possibly lose your job if you don't produce enough code that actually runs. So, because of market pressures, the difficulty of the task and lack of easy-to-use (and affordable) tools, modeling and design go by the wayside. Hence, the appearance that UML isn't needed.



## Design, Modelling and Reverse Engineering 