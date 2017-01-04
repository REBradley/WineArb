import React from "react";

import { CustomJTron } from "./articles";

import Title from "./components/title.js";
import Text from "./components/text.js";
import LinkButton from "./components/button.js";

const Services = CustomJTron(Title, LinkButton);

const AppCopy = (
    <div>
        <h3>Summary:</h3>
        <p>
            The year is 2017, and your customers spend more time on their phones than ever doing everything.
            It is important for companies to have a platform that is optimized for every
            device; a hub that connects everything you do with the people who love what you do.
            It enables what we call CRM, Customer Relationship Management. Web Apps are at
            the heart of this concept, laying the foundation for tools bridging the gap between physical and digital.
        </p>
        <h3>Features:</h3>
        <ul>
            <li>Mobile, tablet, desktop optimized</li>
            <li>User Management</li>
            <li>Excellent menu, product display</li>
            <li>Extendable and Customizable</li>
        </ul>
        <h3>Ultimately:</h3>
        <ul>
            <li>Easily launch new profit centers</li>
            <li>Increase ROI on existing ones</li>
        </ul>
        <h3>Demos:</h3>
        <ul>
            <li><a href="https://vinarb.herokuapp.com">Featured wine + wine and beer lists</a></li>
        </ul>
    </div>
);

const Email = (
    <div>
        <h3>Summary:</h3>
        <p>
            Reach out to your customers regularly with polished emails, and collect
            data for all your campaigns. You can quickly sell large quantities of merchandise,
            remind them you are there for them, and build brand loyalty. Email is a powerful
            tool because it works both ends of the product pipeline: capture lower per unit
            cost via volume discounts, and move volume quickly. All this with lower risk
            to you because through your email campaign, we can track emails to see how
            many were opened, if customers clicked on any items, and how many went to go visit your
            Web App as a result. We make sure that the email actually gets there, on time, looking great.
        </p>
        <h3>Features:</h3>
        <ul>
            <li>Attractive, professional email</li>
            <li>Track opens and clicks</li>
            <li>Mobile, tablet, desktop optimized</li>
        </ul>
        <h3>Ultimately:</h3>
        <ul>
            <li>Preferentially move high margin items</li>
            <li>Drive traffic to store</li>
            <li>Drive traffic to Web App</li>
            <li>Grow your brand</li>
        </ul>
    </div>
);

const WineList = (
    <div>
        <h3>Summary:</h3>
        <p>
            Whether you have 1 or 100 pages of wines to sell, allowing your customers to easily navigate your offerings
            should be your top priority. Often times website designers fail to deliver an easy to scan, fully informative
            list of your wines. Or worse yet, you still use a pdf to show your stuff online. It no lomger has to be this
            way... use the wine list made by a wine professional, for wine professionals and their customers.
        </p>
        <h3>Features:</h3>
        <ul>
            <li>Attractive, scannable wine listings</li>
            <li>Full information including abv, grape(s), region, price</li>
            <li>VinArb updates the list for you</li>
        </ul>
        <h3>Ultimately:</h3>
        <ul>
            <li>Provide your customers with the best way to explore your list</li>
            <li>Forget about updating your online wine list</li>
            <li>Forget about updating your wine list and save on paper waste</li>
        </ul>
    </div>
);

const Review = (
    <div>
        <h3>Summary:</h3>
        <p>
            Keep track of all the wines you try. VinArb provides a free wine review app for all members.
        </p>
        <h3>Features:</h3>
        <ul>
            <li>Easily and quickly add reviews</li>
            <li>Grape, Region, Producer and other information is added for you</li>
            <li>Filter by score</li>
            <li>All of your images are stored in the cloud with Amazon Web Services</li>
        </ul>
        <h3>Ultimately:</h3>
        <ul>
            <li>Remember what you like</li>
            <li>Practice your wine description skills</li>
            <li>Learn about wine</li>
        </ul>
    </div>
);

const EmailCopy = <Text text={Email} />

const WebAppCopy = <Text text={AppCopy} />

const ReviewCopy = <Text text={Review} />

const WineListCopy = <Text text={WineList} />

export { Services, WebAppCopy, EmailCopy, ReviewCopy, WineListCopy };
