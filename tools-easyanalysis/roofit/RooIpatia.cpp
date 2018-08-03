/***************************************************************************** 
 * Project: RooFit                                                           * 
 *                                                                           * 
 * This code was autogenerated by RooClassFactory                            * 
 *****************************************************************************/ 

// Your description goes here... 

#include "Riostream.h" 

#include "RooIpatia.h" 
#include "RooAbsReal.h" 
#include "RooAbsCategory.h" 
#include <math.h> 
#include <cmath>
#include "TMath.h" 
#include "Math/SpecFunc.h"
#include "Math/IFunction.h"
#include "gsl/gsl_sf_bessel.h"

const Double_t RooIpatia__sq2pi = sqrt(2*acos(-1.0));
const Double_t RooIpatia__sq2pi_inv = 1./RooIpatia__sq2pi;
const Double_t RooIpatia__logsq2pi = log(RooIpatia__sq2pi);
const Double_t RooIpatia__log_de_2 = log(2.0);

Double_t RooIpatia__low_x_BK(Double_t nu,Double_t x){
    return TMath::Gamma(nu)*pow(2,nu-1)*pow(x,-nu);
}


Double_t RooIpatia__low_x_LnBK(Double_t nu, Double_t x){
    return log(TMath::Gamma(nu)) + (nu-1)*RooIpatia__log_de_2 - nu * log(x);
}

Double_t RooIpatia__BK(Double_t ni, Double_t x) {
    Double_t nu = abs(ni);
    if ( x < 1e-06 && nu > 0) return RooIpatia__low_x_BK(nu,x);
    if ( x < 1e-04 && nu > 0 && nu < 55) return RooIpatia__low_x_BK(nu,x);
    if ( x < 0.1 && nu >= 55) return RooIpatia__low_x_BK(nu,x);

    return gsl_sf_bessel_Knu(nu, x);
    //return ROOT::Math::cyl_bessel_k(nu, x);
}

Double_t RooIpatia__LnBK(double ni, double x) {
    Double_t nu = abs(ni);
    if ( x < 1e-06 && nu > 0) return RooIpatia__low_x_LnBK(nu,x);
    if ( x < 1e-04 && nu > 0 && nu < 55) return RooIpatia__low_x_LnBK(nu,x);
    if ( x < 0.1 && nu >= 55) return RooIpatia__low_x_LnBK(nu,x);

    return gsl_sf_bessel_lnKnu(nu, x);
    //return ROOT::Math::cyl_bessel_k(nu, x);
}

// Double_t eval(Double_t d, Double_t l, Double_t alpha, Double_t beta, Double_t delta, Double_t mu) {
//   Double_t RooIpatia__sq2pi = sqrt(2*acos(-1));
//   Double_t cons1 = 1./RooIpatia__sq2pi;
//   Double_t gamma = alpha;// sqrt(alpha*alpha-beta*beta);
//   Double_t dg = delta*gamma;
//   //Double_t mu_ = mu;// - delta*beta*RooIpatia__BK(l+1,dg)/(gamma*RooIpatia__BK(l,dg));
//   //Double_t d = x-mu;
//   Double_t thing = sqrt(delta*delta + d*d);
//   Double_t no = pow(gamma/delta,l)/RooIpatia__BK(l,dg)*cons1;
//   Double_t num = no*RooIpatia__BK(l-0.5,thing*alpha);
//   Double_t den = pow(thing/alpha,0.5-l);
//   Double_t cheat = exp(beta*d);//*(abs(beta) + 0.0001);
//  return  cheat*num/den ;
// }

Double_t RooIpatia__LogEval(Double_t d, Double_t l, Double_t alpha, Double_t beta, Double_t delta) {
    //Double_t d = x-mu;
    //Double_t RooIpatia__sq2pi = sqrt(2*acos(-1));
    Double_t gamma = alpha;//sqrt(alpha*alpha-beta*beta);
    Double_t dg = delta*gamma;
    Double_t thing = delta*delta + d*d;
    Double_t logno = l*log(gamma/delta) - RooIpatia__logsq2pi -RooIpatia__LnBK(l, dg);
    /*printf("%e\n",exp(logno));
      printf("%e\n",RooIpatia__LnBK(l-0.5,alpha*sqrt(thing)));
      printf("%e\n",(0.5-l)*(log(alpha)-0.5*log(thing)));
      printf("%e\n", logno + beta*d +(0.5-l)*(log(alpha)-0.5*log(thing)) + RooIpatia__LnBK(l-0.5,alpha*sqrt(thing)));
      printf("%e\n", exp(logno + beta*d +(0.5-l)*(log(alpha)-0.5*log(thing)) + RooIpatia__LnBK(l-0.5,alpha*sqrt(thing))));
    */
    return exp(logno + beta*d +(0.5-l)*(log(alpha)-0.5*log(thing)) + RooIpatia__LnBK(l-0.5,alpha*sqrt(thing)));// + log(abs(beta)+0.0001) );

}

Double_t RooIpatia__diff_eval(Double_t d, Double_t l, Double_t alpha, Double_t beta, Double_t delta){
    //Double_t RooIpatia__sq2pi = sqrt(2*acos(-1));
    //Double_t cons1 = 1./RooIpatia__sq2pi;
    Double_t gamma = alpha;// sqrt(alpha*alpha-beta*beta);
    Double_t dg = delta*gamma;
    //Double_t mu_ = mu;// - delta*beta*BK(l+1,dg)/(gamma*BK(l,dg));
    //Double_t d = x-mu;
    Double_t thing = delta*delta + d*d;
    Double_t sqthing = sqrt(thing);
    Double_t alphasq = alpha*sqthing;
    Double_t no = pow(gamma/delta,l)/RooIpatia__BK(l,dg)*RooIpatia__sq2pi_inv;
    Double_t ns1 = 0.5-l;
    //Double_t cheat = exp(beta*d);//*(abs(beta) + 1e-04);
    //Double_t cheat = exp(beta*d);//*(abs(beta) + 0.0001);

    //no =  no*pow(alpha, ns1 )*pow(thing, 0.5*l - 5.0/4.0)*0.5*cheat;//exp(beta*d);

    //return no*(-alphasq*d* (RooIpatia__BK(l - 3.0/2.0, alphasq) - RooIpatia__BK(l + 0.5, alphasq)) + (2*beta*thing + 2*d*l - d)*RooIpatia__BK(-ns1, alphasq));
    //return no*pow(alpha, -l + 1.0/2.0)*pow(thing, l/2 - 5.0/4.0)*(-d*alphasq*RooIpatia__BK(l - 3.0/2.0, alphasq) - d*alphasq*RooIpatia__BK(l + 1.0/2.0, alphasq) + 2*beta*thing*RooIpatia__BK(l - 0.5, alphasq) + 2*d*l*RooIpatia__BK(l - 0.5, alphasq) - d*RooIpatia__BK(l - 0.5, alpha*sqthing))*exp(beta*d)/2;
  
    return no*pow(alpha, ns1)*pow(thing, l/2 - 5.0/4.0)*(-d*alphasq*(RooIpatia__BK(l - 3.0/2.0, alphasq) + RooIpatia__BK(l + 0.5, alphasq)) + (2*(beta*thing + d*l) - d)*RooIpatia__BK(ns1, alphasq))*exp(beta*d)/2;
}



ClassImp(RooIpatia) 

RooIpatia::RooIpatia(const char *name, const char *title, 
		     RooAbsReal& _x,
		     RooAbsReal& _l,
		     RooAbsReal& _zeta,
		     RooAbsReal& _fb,
		     RooAbsReal& _sigma,
		     RooAbsReal& _mu,
		     RooAbsReal& _a,
		     RooAbsReal& _n) :
RooAbsPdf(name,title), 
    x("x","x",this,_x),
    l("l","l",this,_l),
    zeta("zeta","zeta",this,_zeta),
    fb("fb","fb",this,_fb),
    sigma("sigma","sigma",this,_sigma),
    mu("mu","mu",this,_mu),
    a("a","a",this,_a),
    n("n","n",this,_n)
{ 
} 

RooIpatia::RooIpatia(const RooIpatia& other, const char* name) :  
    RooAbsPdf(other,name), 
    x("x",this,other.x),
    l("l",this,other.l),
    zeta("zeta",this,other.zeta),
    fb("fb",this,other.fb),
    sigma("sigma",this,other.sigma),
    mu("mu",this,other.mu),
    a("a",this,other.a),
    n("n",this,other.n)
{ 
} 

Double_t RooIpatia::evaluate() const 
{ 
    Double_t d = x-mu;
    Double_t cons0 = sqrt(zeta);
    Double_t alpha, beta, delta,  cons1, phi, A, B, k1, k2;
    Double_t asigma = a*sigma;
    Double_t out = 0.0;
    if (zeta!= 0.) {
	phi = RooIpatia__BK(l+1,zeta)/RooIpatia__BK(l,zeta); // careful if zeta -> 0. You can implement a function for the ratio, but carefull again that |nu + 1 | != |nu| + 1 so you jave to deal wiht the signs
	cons1 = sigma/sqrt(phi);
	alpha  = cons0/cons1;//*sqrt((1 - fb*fb));
	beta = fb;//*alpha;
	//gamma = sqrt(alpha*alpha - beta*beta);
	delta = cons0*cons1;
	//printf("%e\n",phi);
	//printf("%e\n",cons0);
	//printf("%e\n",cons1);
	//printf("%e\n",exp(beta*d));
	//printf("%e\n",alpha);
	//printf("%e\n",delta);
	//printf("%e\n",RooIpatia__LogEval(x,l,alpha,beta,delta, mu));
     
	if (d > -asigma ) return RooIpatia__LogEval(d,l,alpha,beta,delta);
	k1 = RooIpatia__LogEval(-asigma,l,alpha,beta,delta);
	k2 = RooIpatia__diff_eval(-asigma,l,alpha,beta,delta);
	B = -asigma + n*k1/k2;
	A = k1*pow(B+asigma,n);
	out =  A*pow(B-d,-n);
	//return RooIpatia__LogEval(x,l,alpha,beta,delta, mu);
    }
    else if (l < 0) {
	beta = fb;
	cons1 = -2*l;
	delta = sigma;
	if (d > -asigma ) return  exp(beta*d)*pow(1 + d*d/(delta*delta),l-0.5);
	cons1 = exp(-beta*asigma);
	phi = 1 + a*a;
	k1 = cons1*pow(phi,l-0.5);
	k2 = beta*k1- cons1*(l-0.5)*pow(phi,l-1.5)*2*a/delta;
	B = -asigma + n*k1/k2;
	A = k1*pow(B+asigma,n);
	out = A*pow(B-d,-n);
    }
    return out;
} 