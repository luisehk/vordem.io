import Link from 'next/link'
import Layout from '../components/layout'

const About = () => (
  <Layout>
    
	<section className="pt60">
	  <div className="l-wrapp-hidden-widescreen pb80">
	    <div className="columns">
	      <div className="column is-half pr70">
	        <h1 className="txt48 mb50">
	          <strong>What we do</strong>
	        </h1>
	        <p className="mb40">
	            We create great digital products by taking the best out of design, technology and strategy, which means having a team with a variety of skills following a structured process to continuously deliver value to your business.
	        </p>

	        <a className="icon-arrow-button-down"></a>
	      </div>
	      <div className="column is-half is-flex-tablet">
	        <div className="is-right has-img">
	          <img src="/static/img/working.svg" alt="" />
	        </div>
	      </div>
	    </div>
	  </div>
	</section>

	<section className="bg-red-gradient has-texture pt60 pb80">
	    <div className="wrap">
	        <div className="columns">
	            <div className="column is-two-thirds pr70">
	                <img src="/static/img/brainstorm-meeting.jpg" alt="" />
	            </div>
	            <div className="column is-one-thirds">
	                <p className="txt18 c-white">1/4</p>
	                <h1 className="txt36 mb20 c-white"><strong>Discover & Conceptualize</strong></h1>

	                <p className="mb40 c-white">Using different tools like Design Sprint, User Experience Design and Product Management, we focus on ensuring that the software solves a real problem in a way that is helpful to your users and your business.</p>

	                <div className="c-white">
	                  <strong>Outcomes / Deliverables:</strong>
	                  <ul className="mb40 c-white">
	                    <li>Product brief</li>
	                    <li>Customer journey map</li>
	                    <li>Low-fidelity wireframes</li>
	                    <li>Real-looking prototype</li>
	                    <li>Findings from the user testing</li>
	                    <li>Report with next steps</li>
	                  </ul>
	                </div>
	            </div>
	        </div>
	    </div>
	</section>

	<section className="bg-white has-texture pt60 pb80">
	    <div className="wrap">
	        <div className="columns">
	            <div className="column is-one-thirds">
	                <p className="txt18">2/4</p>
	                <h1 className="txt36 mb20"><strong>Plan & Design</strong></h1>

	                <p className="mb40">Once we have enough certainty about the product, we polish the interface design, write detailed user stories, prioritize features, do data modeling, etc. The goal is to know what's needed to build the product and give the development team what they need to do so.</p>

	                <div>
	                  <strong>Outcomes / Deliverables:</strong>
	                  <ul className="mb40">
	                    <li>Detailed user stories</li>
	                    <li>Acceptance criteria</li>
	                    <li>Revised wireframes</li>
	                    <li>System architecture</li>
	                    <li>Database design</li>
	                    <li>Finished UI design</li>
	                  </ul>
	                </div>
	            </div>
	            <div className="column is-two-thirds pl70">
	                <img src="/static/img/software-development-planning-session.jpg" alt="" />
	            </div>
	        </div>
	    </div>
	</section>

	<section className="bg-blue-gradient has-texture pt60 pb80">
	    <div className="wrap">
	        <div className="columns">
	            <div className="column is-two-thirds pr70">
	                <img src="/static/img/coding.jpg" alt="" />
	            </div>
	            <div className="column is-one-thirds">
	                <p className="txt18 c-white">3/4</p>
	                <h1 className="txt36 mb20 c-white"><strong>Build & Launch</strong></h1>

	                <p className="mb40 c-white">This is where we focus on the actual development of the product, applying industries' best practices such as test-driven development, continuous integration / deployment, short iterations, code review, among others.</p>

	                <div className="c-white">
	                  <strong>Outcomes / Deliverables:</strong>
	                  <ul className="mb40 c-white">
	                    <li>Shipped funcionality every two weeks</li>
	                    <li>Weekly project status</li>
	                    <li>Stable & maintainable codebase</li>
	                    <li>User manual</li>
	                    <li>Full source code</li>
	                  </ul>
	                </div>
	            </div>
	        </div>
	    </div>
	</section>

	<section className="bg-white has-texture pt60 pb80">
	    <div className="wrap">
	        <div className="columns">
	            <div className="column is-one-thirds">
	                <p className="txt18">4/4</p>
	                <h1 className="txt36 mb20"><strong>Iterate & Scale</strong></h1>

	                <p className="mb40">When your digital product is released you need to keep making improvements to it: optimizations, new features, improvements to existing features, automate backups, track KPIs, among other things. That's why after shipping your product we continue to work together on a retainer fee, so you can focus on growing your business while we take care of the technology.</p>

	                <div>
	                  <strong>Outcomes / Deliverables:</strong>
	                  <ul className="mb40">
	                    <li>New releases every two weeks</li>
	                    <li>Product management</li>
	                    <li>Development operations</li>
	                    <li>Application performance monitoring</li>
	                  </ul>
	                </div>
	            </div>
	            <div className="column is-two-thirds pl70">
	                <img src="/static/img/laptops.jpg" alt="" />
	            </div>
	        </div>
	    </div>
	</section>

	<section className="bg-green-gradient has-texture c-white ptb60">
	  <div className="wrap">
	    <div className="columns">
	      <div className="column is-align-middle has-text-centered">
	        <h1 className="txt36 mb20"><strong>Ready to take your business to the next level?</strong></h1>

	        <Link href="/work">
	        	<a className="button bg-white c-red has-arrow is-right mb20">View our work</a>
	        </Link>

	        <Link href="/contact">
	        	<a className="button bg-red c-white has-arrow is-right mb20">Request Quote</a>
	      	</Link>
	      </div>
	    </div>
	  </div>
	</section>

  </Layout>
)

export default About
