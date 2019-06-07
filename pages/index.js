import Link from 'next/link'
import Layout from '../components/layout'

const Index = () => (
  <Layout>
    <section className="pt60">
      <div className="l-wrapp-hidden-widescreen pb80">
        <div className="columns">
          <div className="column is-half pr70">
            <h1 className="txt48 mb50">
              <strong>We create digital products that help businesses reach their full potential</strong>
            </h1>
            <p className="mb40">
              Vordem is a digital product agency, founded with the mission of making businesses thrive by doing what we do best: technology. This means working at the intersection of business, creativity and technology through a structured innovation process with a clear goal in mind: making things happen.
            </p>
            <a className="icon-arrow-button-down"></a>
          </div>
          <div className="column is-half is-flex-tablet">
            <div className="is-right has-img">
              <img src="/static/img/img1-1.svg" alt="" />
            </div>
          </div>
        </div>
      </div>
      <div className="wrap">
        <div className="columns">
          <div className="column is-two-thirds pr70">
            <img src="/static/img/pic1.jpg" alt="" />
          </div>
          <div className="column is-one-thirds">
            <h1 className="txt36 mb20"><strong>A balanced approach</strong></h1>
            <p className="mb40">
              Successful digital products come from the focused collaboration of strategists, developers, designers and product managers, working together to craft simple and elegant solutions to complex challenges.
            </p>
            <Link href="/about">
              <a className="button bg-red c-white has-arrow is-right">Learn more</a>
            </Link>
          </div>
        </div>
      </div>
    </section>

    <section className="bg-blue-gradient has-texture ptb60 mt60">
      <div className="wrap">
        <h4 className="c-white txt36 mb40"><strong>Recent projects</strong></h4>

        <div className="columns pb20">

          <div className="column is-one-third">
            <div className="square-card">
              <a href="#">
                <div className="img">
                  <img src="/static/img/portfolio/comex/thumbnail.png" alt="Publicomex" />
                </div>
                <div className="title"><h3 className="txt26"><strong>Publicomex</strong></h3></div>
              </a>
            </div>
          </div>

          <div className="column is-one-third">
            <div className="square-card">
              <a href="#">
                <div className="img">
                  <img src="/static/img/portfolio/sealedair/thumbnail.png" alt="Sealed Air" />
                </div>
                <div className="title"><h3 className="txt26"><strong>Sealed Air</strong></h3></div>
              </a>
            </div>
          </div>

          <div className="column is-one-third">
            <div className="square-card">
              <a href="#">
                <div className="img">
                  <img src="/static/img/portfolio/santander/thumbnail.png" alt="Premio Santander" />
                </div>
                <div className="title"><h3 className="txt26"><strong>Premio Santander</strong></h3></div>
              </a>
            </div>
          </div>
        </div>
        <div className="columns">
          <div className="column is-flex-tablet">
            <Link href="/work">
              <a className="button bg-white c-red has-arrow is-right">View our work</a>
            </Link>
          </div>
        </div>
      </div>
    </section>

    <section className="bg-white ptb60">
      <div className="wrap">
        <div className="columns pb80">
          <div className="is-one-third column">
            <h4 className="txt36 mb40"><strong>Our clients</strong></h4>
            <p>We've worked with startups and big companies from different industries: transportation, finance, information technology, retail, education and others.</p>
          </div>
        </div>
        <div className="columns">
          <div className="column is-12">
            <div className="has-inline-list has-logo-list has-text-centered-tablet">
              <div className="img is-grayscale is-half-inline">
                <img src="/static/img/icon-logo8.png" alt="" />
              </div>
              <div className="img is-grayscale is-half-inline">
                <img src="/static/img/icon-logo3.png" alt="" />
              </div>
              <div className="img is-grayscale is-half-inline">
                <img src="/static/img/icon-logo10.png" alt="" />
              </div>
              <div className="img is-grayscale is-half-inline">
                <img src="/static/img/icon-logo1.png" alt="" />
              </div>
              <div className="img is-grayscale is-half-inline">
                <img src="/static/img/icon-logo4.png" alt="" />
              </div>
              <div className="img is-grayscale is-half-inline">
                <img src="/static/img/icon-logo2.png" alt="" />
              </div>
              <div className="img is-grayscale is-half-inline">
                <img src="/static/img/icon-logo7.png" alt="" />
              </div>
              <div className="img is-grayscale is-half-inline">
                <img src="/static/img/icon-logo5.png" alt="" />
              </div>
              <div className="img is-grayscale is-half-inline">
                <img src="/static/img/icon-logo6.png" alt="" />
              </div>
              <div className="img is-grayscale is-half-inline">
                <img src="/static/img/icon-logo9.svg" alt="" />
              </div>
              <div className="img is-grayscale is-half-inline">
                <img src="/static/img/icon-logo11.png" alt="" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section className="bg-green-gradient has-texture c-white ptb60">
      <div className="wrap">
        <div className="columns">
          <div className="column is-align-middle has-text-centered">
            <h1 className="txt36 mb20"><strong>Ready to take your business to the next level?</strong></h1>

            <Link href="/about">
              <a className="button bg-white c-red has-arrow is-right mb20">More about us</a>
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

export default Index