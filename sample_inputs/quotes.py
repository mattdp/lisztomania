class Quotes:

    # not sure what output format helps most yet
    def get_quotes(quantity):
        quotes = Quotes.quotes_list()
        length = len(quotes)

        #TODO get X nonoverlapping random integers. for continuity assuming q = 2
        rands = [4,11]

        result = []
        for q in range(0,quantity):
            result.append(quotes[rands[q]])
        return result

    def quotes_list():
        quotes = [
            ["The quality of your questions determines the quality of your life.","Tony Robbins"],
            ["Being a professional is doing the things you love to do, on the days you don't feel like doing them.","Juilus Irving"],
            ["If you find yourself in a fair fight, you didn't plan your mission properly.","Colonel David Hackworth"],
            ["In negotiation, he who cares the least wins.","Tim Ferriss"],
            ["As you survey the challenges of your life, ask 'which of these did you assign yourself, and which are you doing to please someone else?'","Chris Sacca"],
            ["Don't write to please anyone but yourself. The second you start doing it for an audience, you've lost the long game, because creating something reliable and sustainable over the long run requires, most of all, keeping yourself excited about it.","Maria Popova"],
            ["The moment when you feel that, just possibly, you're walking down the street naked, exposing too much of your heart and mind and what exists on the inside, showing too much of yourself. That's the moment you may be starting to get it right.","Neil Gaiman"],
            ["What you do is more important than how [much] you do everything else, and doing something well does not make it important.","Tim Ferriss"],
            ["Investing in yourself is the most important investment you'll ever make in your life...there's no financial investment that'll ever match it, because if you develop more skill, more ability, more insight, more capacity, that's what's really going to provide economic freedom.","Warren Buffet"],
            ["Is this really a problem I need to think my way out of? Or is it possible I just need to fix my biochemisty?","Tim Ferriss"],
            ["If you can describe the problem better than your target customer, they will automatically assume you have the solution.","Jay Abraham"],
            ["If life-transforming missions could be found with just a little navel-gazing and an optimistic attitude, changing the world would be commonplace.","Cal Newport"],
            ["Time is the coin of your life. It is the only coin you have, and only you can determine how it will be spent. Be careful, lest you let other people spend it for you.","Carl Sandberg"],
            ["A man who dares waste an hour of time has not yet discovered the value of life.","Charles Darwin"],
            ["Your body is designed for success in the past. It is an antique biological machine that evolved in response to a world that no longer exists.","Zimbardo"],
            ["We're surrounded by people who are busy getting their ducks in a row, waiting for just the right moment. Getting your ducks in a row is a fine thing to do. But deciding what you are going to do with that duck is a far more important issue.","Seth Godin"],
            ["Success is fundamentally about how you spend your time.","Taylor Pearson"],
        ]
        return quotes