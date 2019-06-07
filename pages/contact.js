import Link from 'next/link'
import Layout from '../components/layout'

const Contact = () => (
  <Layout>

	<section className="pt60">
	  <div className="l-wrapp-hidden-widescreen pb80">
	    <div className="columns">
	      <div className="column is-half pr70">
	        <h1 className="txt48 mb50">
	          <strong>Let's talk</strong>
	        </h1>
	        <p className="mb40">
	            All great projects start with a Hello.
	        </p>
	        <p className="mb40">
	            Tell us about your project by sending an email to <a href="mailto:hello@vordem.io" className="c-black"><strong>hello@vordem.io</strong></a>. 
	            <br />Please add as much detail as possible: 
	            <br />What's your idea?
	            <br />What's the goal of the project? 
	            <br />Is there a deadline you need to meet?
	        </p>

	        <a className="icon-arrow-button-down"></a>
	      </div>
	      <div className="column is-half is-flex-tablet">
	        <div className="is-right has-img">
	          <img src="/static/img/conversation.svg" alt="" />
	        </div>
	      </div>
	    </div>
	  </div>
	</section>

	<section className="bg-red-gradient has-texture pt60 pb80-mobile">
	    <div className="wrap">
	        <div className="columns">
	            <div className="column is-two-thirds pr70">
	                <div className="has-iframe">
	                    <iframe
	                    	src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3595.480933098569!2d-100.35835978452472!3d25.68849601789526!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8662960eb9f1f3bd%3A0xadbd994030146264!2sBolivia+203%2C+Vista+Hermosa%2C+64620+Monterrey%2C+N.L.!5e0!3m2!1ses-419!2smx!4v1536189225898"
	                    	width="600"
	                    	height="450"
	                    	frameBorder="0"
	                    	style={{border:0}}
	                    	allowFullScreen></iframe>
	                </div>
	            </div>
	            <div className="column is-one-thirds">
	                <h3 className="txt36 mb20 c-white">
	                	<strong>Where to find us</strong>
	                </h3>
	                <ul className="has-list">
	                    <li className="pb20 c-white">
	                    	<div className="has-icon">
	                    		<img src="/static/img/icon1.svg" alt="" />
	                    	</div>
	                    	<p>
	                    		Bolivia #203<br />
	                    		Vista Hermosa C.P. 64620<br />
	                    		Monterrey, NL. México
	                    	</p>
	                    </li>
	                    <li className="pb20 c-white">
	                        <div className="has-icon">
	                        	<img src="/static/img/icon2.svg" alt="" />
	                        </div>
	                        <p>
	                        	<a href="mailto:hello@vordem.io" className="c-white">hello@vordem.io</a>
	                        </p>
	                    </li>
	                    <li className="pb20 c-white"><div className="has-icon"><img src="/static/img/icon3.svg" alt="" /></div><p>+52 81 2473 9607</p></li>
	                </ul>
	            </div>
	        </div>
	    </div>
	</section>


	<section className="bg-white ptb60">
	    <div className="wrap">
	        <div className="columns">
	            <div className="column is-one-third">
	                <h1 className="txt36 mb20"><strong>Interested in working at Vordem?</strong></h1>
	                <p className="mb40">We are always looking for software engineers, UI/UX designers, strategists, data scientists, business developers and product managers eager to make an impact in this world through technology.</p>

	                <p className="mb40">If you're looking for a place where you can work on challenging problems with an exceptional team, let's talk!</p>

	                <a href="mailto:hello@vordem.io" className="is-hidden-mobile button bg-red c-white has-arrow is-right">Drop us an email</a>
	            </div>

	            <div className="column is-two-thirds">
	                <div className="columns">
	                    <div className="column is-flex">
	                        <div className="is-right">
	                            <img src="/static/img/img2.png" alt="" className="has-shadow" />
	                        </div>
	                    </div>
	                </div>
	            </div>

	            <div className="column is-hidden-tablet">
	                <a href="mailto:hello@vordem.io" className="button bg-red c-white has-arrow is-right">Drop us an email</a>
	            </div>
	        </div>
	    </div>
	</section>

  </Layout>
)

export default Contact
