to add this https://github.com/SRINIVASTA here are any where  this one in which path that should open let visits = {}; // Simple in-memory store (resets on redeploy)

export default function handler(req, res) {
  const { app } = req.query;

  if (!app) {
    res.status(400).send('Missing app parameter');
    return;
  }

  visits[app] = (visits[app] || 0) + 1;

  const urls = {
    'quantum-ai-portfolio': 'https://quantum-ai-portfolio-bffydmzkdbtjaejwf6huvh.streamlit.app/',
    'stock-analysis-dashboard': 'https://stockanalysis-mnqhv79yzkrrkai85vft8a.streamlit.app/',
    'multi-agent-chatbot': 'https://multi-agent-chatbot-yv35yj5g7obpbibcxnwrme.streamlit.app/',
    'photo-background-changer': 'https://photo-bg-changer-kdrxyvhjx3ibr4ccoddm3f.streamlit.app/',
    'nifty50-stock-analysis': 'https://nifty50-stock-analysis-cyuz5gmnyxcd48pfxszwdy.streamlit.app/',
    'gemini-ai-image-generator': 'https://gemini-image-generator-bdyowfxxqb4q5htbrrgjzv.streamlit.app/',
    'ai-super-tool': 'https://ai-super-tool-uxhxpvn4lqyc7szmsdqtl8.streamlit.app/',
    'real-time-sales-dashboard': 'https://real-time-sales-dashboard-key6zivh5fnkane3t8x6v2.streamlit.app/',
  };

  const redirectUrl = urls[app];

  if (!redirectUrl) {
    res.status(404).send('App not found');
    return;
  }

  res.writeHead(302, { Location: redirectUrl });
  res.end();
}
 
