// MAS MindForge Well-Architected Lens - Interactive Questionnaire
// v1.1 with AWS Native Service Recommendations

'use strict';

const PILLARS = [
  {
    id: 'oversight',
    name: 'AI Oversight',
    description: 'Governance scope, accountability, and oversight structures',
    questions: [
      {
        id: 'Q1.1',
        title: 'Scope and Application',
        text: 'Is AI governance scope formally defined and operationalized across all AI systems?',
        bestPractices: [
          { text: 'AI governance scope is formally defined and documented', awsServices: ['AWS Organizations', 'AWS Config', 'AWS Audit Manager'] },
          { text: 'AI use cases are inventoried and classified by risk tier', awsServices: ['AWS Config', 'Amazon SageMaker Model Registry', 'AWS Resource Explorer'] },
          { text: 'Distinction between traditional AI, GenAI, and agentic AI is operationalized', awsServices: ['AWS Config Rules', 'Amazon Bedrock', 'Amazon SageMaker'] }
        ],
        improvementPlan: 'Establish a formal AI governance charter that defines scope, creates an inventory of all AI systems, and operationalizes distinctions between AI types. Use AWS Config to track AI resources and AWS Audit Manager to document governance scope.'
      },
      {
        id: 'Q1.2',
        title: 'Responsibilities for AI Oversight',
        text: 'Are AI oversight responsibilities clearly assigned across the three lines of defence?',
        bestPractices: [
          { text: 'Board or equivalent body has AI oversight accountability', awsServices: ['AWS IAM', 'Amazon QuickSight', 'AWS Audit Manager'] },
          { text: 'Three Lines of Defence model is applied to AI risk', awsServices: ['AWS IAM', 'AWS Organizations', 'Amazon CloudWatch'] },
          { text: 'AI ethics or risk committee is established', awsServices: ['AWS IAM', 'Amazon Chime', 'AWS Systems Manager'] }
        ],
        improvementPlan: 'Establish clear accountability for AI governance by assigning board-level oversight, implementing the Three Lines of Defence model, and creating an AI ethics committee. Use AWS IAM for role-based access and Amazon QuickSight for governance dashboards.'
      }
    ]
  },
  {
    id: 'risk',
    name: 'AI Risk Management',
    description: 'Policies, enterprise risk, third-party, use case, and inventory',
    questions: [
      {
        id: 'Q2.1',
        title: 'AI-Related Policies and Standards',
        text: 'Are AI-related policies, procedures, and standards documented and approved?',
        bestPractices: [
          { text: 'AI policy framework is formally approved and communicated', awsServices: ['AWS Audit Manager', 'AWS Config', 'AWS Security Hub'] },
          { text: 'Model risk management standards are defined', awsServices: ['Amazon SageMaker Model Cards', 'Amazon SageMaker Model Monitor', 'AWS CloudTrail'] },
          { text: 'Data governance standards cover AI training and inference data', awsServices: ['Amazon Macie', 'AWS Glue', 'Amazon S3'] }
        ],
        improvementPlan: 'Develop and approve a comprehensive AI policy framework that covers model risk management and data governance. Use AWS Audit Manager for policy documentation and Amazon SageMaker Model Cards for model governance.'
      },
      {
        id: 'Q2.2',
        title: 'Organisation-Level Risk Management',
        text: 'Is AI risk integrated into the enterprise risk management framework?',
        bestPractices: [
          { text: 'AI risk is integrated into enterprise risk taxonomy', awsServices: ['Amazon SageMaker Model Cards', 'AWS Trusted Advisor', 'AWS Cost Explorer'] },
          { text: 'Materiality scoring for AI use cases is operationalized', awsServices: ['Amazon SageMaker Clarify', 'Amazon CloudWatch', 'AWS X-Ray'] },
          { text: 'AI risk appetite statement is defined and approved', awsServices: ['AWS Audit Manager', 'Amazon QuickSight', 'AWS Config'] }
        ],
        improvementPlan: 'Integrate AI risk into the enterprise risk taxonomy with materiality scoring and a defined risk appetite statement. Use SageMaker Clarify for bias detection and Amazon QuickSight for risk dashboards.'
      },
      {
        id: 'Q2.3',
        title: 'Third Party AI Risk Management',
        text: 'Are risks from third-party AI services, models, and data providers managed?',
        bestPractices: [
          { text: 'Third-party AI vendor assessment framework exists', awsServices: ['AWS Artifact', 'AWS Marketplace', 'AWS PrivateLink'] },
          { text: 'Cloud AI service agreements include risk provisions', awsServices: ['AWS Artifact', 'AWS Certificate Manager', 'AWS PrivateLink'] }
        ],
        improvementPlan: 'Implement a third-party AI vendor assessment framework and ensure cloud AI service agreements include risk provisions. Use AWS Artifact for compliance documentation and AWS PrivateLink for secure connectivity.'
      },
      {
        id: 'Q2.4',
        title: 'Use Case-Level AI Risk Management',
        text: 'Is AI risk assessed and managed at the individual use case level?',
        bestPractices: [
          { text: 'AI risk assessments are conducted per use case', awsServices: ['Amazon SageMaker Model Cards', 'Amazon Bedrock Guardrails', 'Amazon Macie'] },
          { text: 'AI Cards or equivalent risk documents are maintained', awsServices: ['Amazon SageMaker Model Cards', 'AWS Systems Manager', 'Amazon S3'] },
          { text: 'Use case risk ratings are reviewed periodically', awsServices: ['Amazon SageMaker Model Monitor', 'Amazon CloudWatch', 'AWS Lambda'] }
        ],
        improvementPlan: 'Conduct per-use-case AI risk assessments and maintain AI Cards for each system. Use SageMaker Model Cards for documentation and SageMaker Model Monitor for ongoing validation.'
      },
      {
        id: 'Q2.5',
        title: 'AI Inventory Capabilities',
        text: 'Is a comprehensive inventory of AI assets maintained with appropriate metadata?',
        bestPractices: [
          { text: 'AI inventory system is implemented and maintained', awsServices: ['AWS Config', 'Amazon SageMaker Model Registry', 'AWS Resource Explorer'] },
          { text: 'Inventory captures model lineage, ownership, and risk tier', awsServices: ['Amazon SageMaker Model Registry', 'AWS Glue', 'Amazon DynamoDB'] }
        ],
        improvementPlan: 'Implement an AI inventory system that captures model lineage, ownership, and risk tier. Use AWS Config for resource tracking and SageMaker Model Registry for model versioning.'
      }
    ]
  },
  {
    id: 'lifecycle',
    name: 'AI Lifecycle Management',
    description: 'Context, data, build, deploy, and monitoring',
    questions: [
      {
        id: 'Q3.1',
        title: 'Use Case Context and Design',
        text: 'Is use case context and design defined before development begins?',
        bestPractices: [
          { text: 'Business problem and success metrics are defined', awsServices: ['Amazon SageMaker', 'Amazon Bedrock', 'AWS Systems Manager'] },
          { text: 'Fairness and bias assessment is conducted at design stage', awsServices: ['Amazon SageMaker Clarify', 'Amazon Bedrock Guardrails', 'AWS Lambda'] }
        ],
        improvementPlan: 'Define business problems and success metrics before development. Conduct fairness and bias assessments at the design stage using SageMaker Clarify and Bedrock Guardrails.'
      },
      {
        id: 'Q3.2',
        title: 'Data Acquisition and Processing',
        text: 'Is data quality, provenance, and privacy managed throughout the lifecycle?',
        bestPractices: [
          { text: 'Data lineage and provenance are tracked', awsServices: ['AWS Glue', 'Amazon S3', 'AWS Lake Formation'] },
          { text: 'Data quality assessment processes are in place', awsServices: ['AWS Glue DataBrew', 'Amazon CloudWatch', 'AWS Lambda'] },
          { text: 'Privacy and consent requirements are addressed', awsServices: ['Amazon Macie', 'AWS KMS', 'Amazon S3'] }
        ],
        improvementPlan: 'Implement data lineage tracking, quality assessments, and privacy controls. Use AWS Glue for data cataloging, Amazon Macie for privacy scanning, and AWS KMS for encryption.'
      },
      {
        id: 'Q3.3',
        title: 'Onboarding, Build, and Review',
        text: 'Are rigorous development practices including validation and independent review applied?',
        bestPractices: [
          { text: 'Model validation and testing protocols are defined', awsServices: ['Amazon SageMaker Clarify', 'Amazon SageMaker Model Monitor', 'AWS CodePipeline'] },
          { text: 'Independent model review or validation is conducted', awsServices: ['Amazon SageMaker Model Cards', 'AWS CodeBuild', 'Amazon CloudWatch'] },
          { text: 'Documentation of model assumptions and limitations exists', awsServices: ['Amazon SageMaker Model Cards', 'AWS Systems Manager', 'Amazon S3'] }
        ],
        improvementPlan: 'Define model validation protocols, conduct independent reviews, and document assumptions. Use SageMaker Clarify for bias testing and SageMaker Model Cards for documentation.'
      },
      {
        id: 'Q3.4',
        title: 'Deployment',
        text: 'Is the transition to production managed with appropriate controls and approvals?',
        bestPractices: [
          { text: 'Deployment approval process includes risk sign-off', awsServices: ['AWS CloudFormation', 'AWS Systems Manager', 'Amazon SNS'] },
          { text: 'Rollback and incident response plans exist', awsServices: ['AWS Lambda', 'Amazon CloudWatch', 'AWS CloudFormation'] }
        ],
        improvementPlan: 'Implement deployment approval workflows with risk sign-off and create rollback plans. Use AWS CloudFormation for infrastructure as code and Amazon CloudWatch for monitoring.'
      },
      {
        id: 'Q3.5',
        title: 'Usage, Monitoring, and Change Management',
        text: 'Is AI performance continuously monitored with drift detection and change management?',
        bestPractices: [
          { text: 'Production monitoring includes performance and fairness metrics', awsServices: ['Amazon CloudWatch', 'Amazon SageMaker Model Monitor', 'AWS X-Ray'] },
          { text: 'Model drift detection is operationalized', awsServices: ['Amazon SageMaker Model Monitor', 'Amazon CloudWatch', 'AWS Lambda'] },
          { text: 'Change management process covers model updates', awsServices: ['AWS CodePipeline', 'Amazon SageMaker Pipelines', 'AWS Systems Manager'] }
        ],
        improvementPlan: 'Operationalize production monitoring with drift detection and implement change management for model updates. Use SageMaker Model Monitor for drift detection and AWS CodePipeline for CI/CD.'
      }
    ]
  },
  {
    id: 'enablers',
    name: 'Enablers',
    description: 'Skills, knowledge, culture, and infrastructure',
    questions: [
      {
        id: 'Q4.1',
        title: 'Skills, Knowledge, and Culture',
        text: 'Is AI governance supported by appropriate skills, knowledge, and risk-aware culture?',
        bestPractices: [
          { text: 'AI risk training is provided to relevant staff', awsServices: ['AWS Training and Certification', 'Amazon QuickSight', 'Amazon Chime'] },
          { text: 'AI literacy programme covers business and technical staff', awsServices: ['AWS Training and Certification', 'Amazon QuickSight', 'AWS Systems Manager'] }
        ],
        improvementPlan: 'Develop AI risk training programs and AI literacy initiatives for all staff. Use AWS Training and Certification for technical training and Amazon QuickSight for data literacy.'
      },
      {
        id: 'Q4.2',
        title: 'AI Infrastructure',
        text: 'Is the underlying AI infrastructure secure, resilient, and adequate?',
        bestPractices: [
          { text: 'AI development environment is secured and segregated', awsServices: ['Amazon VPC', 'AWS KMS', 'AWS Secrets Manager'] },
          { text: 'Compute and storage resources meet AI workload requirements', awsServices: ['Amazon EC2', 'Amazon S3', 'AWS Auto Scaling'] },
          { text: 'Disaster recovery plans cover AI systems', awsServices: ['AWS Backup', 'Amazon S3', 'AWS CloudFormation'] }
        ],
        improvementPlan: 'Secure and segregate AI development environments, ensure adequate compute and storage, and implement disaster recovery. Use Amazon VPC for network isolation and AWS KMS for encryption.'
      }
    ]
  }
];

const STORAGE_KEY = 'mindforge_wa_v1';

let answers = {};
let notes = {};
let currentPillar = 0;
let currentQuestion = 0;

// Initialize
document.addEventListener('DOMContentLoaded', function() {
  loadState();

  // Show landing page if no answers yet, otherwise show questionnaire
  const hasAnswers = Object.keys(answers).length > 0;
  if (hasAnswers) {
    showQuestionnaire();
    renderSidebar();
    renderQuestion();
    updateProgress();
  }

  setupEventListeners();
});

function loadState() {
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
      const data = JSON.parse(stored);
      answers = data.answers || {};
      notes = data.notes || {};
    }
  } catch (e) {
    console.warn('Failed to load state:', e);
  }
}

function saveState() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({ answers, notes }));
  } catch (e) {
    console.warn('Failed to save state:', e);
  }
}

function getAllQuestions() {
  const questions = [];
  PILLARS.forEach((pillar, pIndex) => {
    pillar.questions.forEach((q, qIndex) => {
      questions.push({
        ...q,
        pillarIndex: pIndex,
        questionIndex: qIndex,
        pillarName: pillar.name,
        pillarId: pillar.id
      });
    });
  });
  return questions;
}

function getCurrentQuestion() {
  const all = getAllQuestions();
  return all[currentQuestion] || null;
}

function renderSidebar() {
  const container = document.getElementById('pillar-list');
  if (!container) return;
  
  let html = '';
  PILLARS.forEach((pillar, pIndex) => {
    const isActive = pIndex === currentPillar;
    html += '<div class="pillar-item">';
    html += '<div class="pillar-header ' + (isActive ? 'active' : '') + '" data-pillar="' + pIndex + '">';
    html += '<span class="pillar-name">' + pillar.name + '</span>';
    html += '<span class="pillar-score">' + pillar.questions.length + ' Qs</span>';
    html += '</div>';
    
    if (isActive) {
      html += '<div class="question-list">';
      pillar.questions.forEach((q, qIndex) => {
        const globalIndex = PILLARS.slice(0, pIndex).reduce((sum, p) => sum + p.questions.length, 0) + qIndex;
        const answer = answers[q.id];
        const isCurrent = globalIndex === currentQuestion;
        html += '<div class="question-item ' + (isCurrent ? 'active' : '') + ' answered-' + (answer || '') + '" data-index="' + globalIndex + '">';
        html += '<span>' + q.id + '</span>';
        html += '</div>';
      });
      html += '</div>';
    }
    
    html += '</div>';
  });
  
  container.innerHTML = html;
  
  // Add click handlers
  container.querySelectorAll('.pillar-header').forEach(header => {
    header.addEventListener('click', () => {
      currentPillar = parseInt(header.dataset.pillar);
      const all = getAllQuestions();
      const firstInPillar = all.findIndex(q => q.pillarIndex === currentPillar);
      if (firstInPillar >= 0) {
        currentQuestion = firstInPillar;
        renderSidebar();
        renderQuestion();
      }
    });
  });
  
  container.querySelectorAll('.question-item').forEach(item => {
    item.addEventListener('click', () => {
      currentQuestion = parseInt(item.dataset.index);
      const q = getCurrentQuestion();
      if (q) {
        currentPillar = q.pillarIndex;
      }
      renderSidebar();
      renderQuestion();
    });
  });
}

function renderQuestion() {
  const q = getCurrentQuestion();
  if (!q) return;
  
  // Update badge and number
  const badge = document.getElementById('current-pillar-badge');
  const number = document.getElementById('question-number');
  const title = document.getElementById('question-title');
  const desc = document.getElementById('question-description');
  const practicesList = document.getElementById('best-practices-list');
  const servicesGrid = document.getElementById('aws-services-grid');
  const improvementText = document.getElementById('improvement-text');
  const notesArea = document.getElementById('notes-textarea');
  
  if (badge) badge.textContent = q.pillarName;
  if (number) number.textContent = 'Question ' + (currentQuestion + 1) + ' of ' + getAllQuestions().length;
  if (title) title.textContent = q.title;
  if (desc) desc.textContent = q.text;
  
  // Best practices
  if (practicesList) {
    practicesList.innerHTML = q.bestPractices.map(bp => '<li>' + bp.text + '</li>').join('');
  }
  
  // AWS Services
  if (servicesGrid) {
    const allServices = q.bestPractices.flatMap(bp => bp.awsServices);
    const unique = [...new Set(allServices)];
    servicesGrid.innerHTML = unique.map(s => '<span class="aws-service-badge">' + s + '</span>').join('');
  }
  
  // Improvement plan
  if (improvementText) {
    improvementText.textContent = q.improvementPlan;
  }
  
  // Notes
  if (notesArea) {
    notesArea.value = notes[q.id] || '';
  }
  
  // Answer buttons
  document.querySelectorAll('.answer-btn').forEach(btn => {
    btn.className = 'answer-btn';
    const val = btn.dataset.value;
    if (answers[q.id] === val) {
      btn.classList.add('selected-' + val);
    }
  });
  
  // Navigation buttons
  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');
  const reportBtn = document.getElementById('report-btn');
  
  if (prevBtn) prevBtn.disabled = currentQuestion === 0;
  if (nextBtn) {
    const all = getAllQuestions();
    nextBtn.style.display = currentQuestion === all.length - 1 ? 'none' : 'inline-block';
  }
  if (reportBtn) {
    const all = getAllQuestions();
    const answered = Object.keys(answers).length;
    reportBtn.style.display = answered >= all.length ? 'inline-block' : 'none';
  }
}

function showQuestionnaire() {
  const landing = document.getElementById('landing-page');
  const questionnaire = document.getElementById('questionnaire-view');
  if (landing) landing.style.display = 'none';
  if (questionnaire) questionnaire.style.display = 'block';
}

function setupEventListeners() {
  // Commence Assessment button
  const commenceBtn = document.getElementById('commence-btn');
  if (commenceBtn) {
    commenceBtn.addEventListener('click', () => {
      showQuestionnaire();
      renderSidebar();
      renderQuestion();
      updateProgress();
    });
  }

  // Answer buttons
  document.querySelectorAll('.answer-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const q = getCurrentQuestion();
      if (!q) return;
      
      answers[q.id] = btn.dataset.value;
      saveState();
      
      document.querySelectorAll('.answer-btn').forEach(b => b.className = 'answer-btn');
      btn.classList.add('selected-' + btn.dataset.value);
      
      updateProgress();
      renderSidebar();
      
      // Auto-advance after short delay
      setTimeout(() => {
        const all = getAllQuestions();
        if (currentQuestion < all.length - 1) {
          currentQuestion++;
          const nextQ = getCurrentQuestion();
          if (nextQ) currentPillar = nextQ.pillarIndex;
          renderSidebar();
          renderQuestion();
        }
      }, 300);
    });
  });
  
  // Notes
  const notesArea = document.getElementById('notes-textarea');
  if (notesArea) {
    notesArea.addEventListener('input', () => {
      const q = getCurrentQuestion();
      if (q) {
        notes[q.id] = notesArea.value;
        saveState();
      }
    });
  }
  
  // Navigation
  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');
  const reportBtn = document.getElementById('report-btn');
  
  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (currentQuestion > 0) {
        currentQuestion--;
        const q = getCurrentQuestion();
        if (q) currentPillar = q.pillarIndex;
        renderSidebar();
        renderQuestion();
      }
    });
  }
  
  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      const all = getAllQuestions();
      if (currentQuestion < all.length - 1) {
        currentQuestion++;
        const q = getCurrentQuestion();
        if (q) currentPillar = q.pillarIndex;
        renderSidebar();
        renderQuestion();
      }
    });
  }
  
  if (reportBtn) {
    reportBtn.addEventListener('click', generateReport);
  }
  
  // Modal
  const modalClose = document.getElementById('modal-close');
  const closeModalBtn = document.getElementById('close-modal-btn');
  const overlay = document.getElementById('modal-overlay');
  
  if (modalClose) modalClose.addEventListener('click', closeModal);
  if (closeModalBtn) closeModalBtn.addEventListener('click', closeModal);
  if (overlay) overlay.addEventListener('click', (e) => {
    if (e.target === overlay) closeModal();
  });
  
  // Export buttons
  const exportCsvBtn = document.getElementById('export-csv-btn');
  const copySummaryBtn = document.getElementById('copy-summary-btn');
  
  if (exportCsvBtn) exportCsvBtn.addEventListener('click', exportCSV);
  if (copySummaryBtn) copySummaryBtn.addEventListener('click', copySummary);
  
  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') {
      const all = getAllQuestions();
      if (currentQuestion < all.length - 1) {
        currentQuestion++;
        const q = getCurrentQuestion();
        if (q) currentPillar = q.pillarIndex;
        renderSidebar();
        renderQuestion();
      }
    } else if (e.key === 'ArrowLeft') {
      if (currentQuestion > 0) {
        currentQuestion--;
        const q = getCurrentQuestion();
        if (q) currentPillar = q.pillarIndex;
        renderSidebar();
        renderQuestion();
      }
    } else if (['1', '2', '3', '4'].includes(e.key)) {
      const values = ['yes', 'partial', 'no', 'na'];
      const btn = document.querySelector('.answer-btn[data-value="' + values[parseInt(e.key) - 1] + '"]');
      if (btn) btn.click();
    }
  });
}

function updateProgress() {
  const all = getAllQuestions();
  const answered = Object.keys(answers).length;
  const progressText = document.getElementById('progress-text');
  const scoreValue = document.getElementById('overall-score');
  
  if (progressText) progressText.textContent = answered + '/' + all.length;
  
  if (answered > 0) {
    const score = calculateOverallScore();
    if (scoreValue) scoreValue.textContent = score + '%';
  }
}

function calculateOverallScore() {
  const all = getAllQuestions();
  let total = 0;
  let count = 0;
  
  const scores = { 'yes': 3, 'partial': 2, 'no': 0 };
  
  all.forEach(q => {
    const ans = answers[q.id];
    if (ans && ans !== 'na') {
      total += scores[ans] || 0;
      count++;
    }
  });
  
  if (count === 0) return 0;
  return Math.round((total / (count * 3)) * 100);
}

function calculatePillarScore(pillarIndex) {
  const pillar = PILLARS[pillarIndex];
  let total = 0;
  let count = 0;
  
  const scores = { 'yes': 3, 'partial': 2, 'no': 0 };
  
  pillar.questions.forEach(q => {
    const ans = answers[q.id];
    if (ans && ans !== 'na') {
      total += scores[ans] || 0;
      count++;
    }
  });
  
  if (count === 0) return 0;
  return Math.round((total / (count * 3)) * 100);
}

function getPostureLabel(score) {
  if (score >= 80) return { label: 'Strong', class: 'posture-strong' };
  if (score >= 60) return { label: 'Moderate', class: 'posture-moderate' };
  if (score >= 40) return { label: 'Developing', class: 'posture-developing' };
  return { label: 'Critical', class: 'posture-critical' };
}

function generateReport() {
  const overall = calculateOverallScore();
  const posture = getPostureLabel(overall);
  const all = getAllQuestions();
  
  let html = '';
  
  // Summary
  html += '<div class="report-summary">';
  html += '<div class="report-score">' + overall + '%</div>';
  html += '<div class="report-label">Overall Maturity Score</div>';
  html += '<div class="report-posture ' + posture.class + '">' + posture.label + ' Posture</div>';
  html += '</div>';
  
  // Pillar scores
  html += '<h3>Domain Scores</h3>';
  html += '<div class="pillar-scores-grid">';
  PILLARS.forEach((pillar, index) => {
    const score = calculatePillarScore(index);
    const fillClass = score >= 80 ? 'fill-green' : score >= 60 ? 'fill-amber' : 'fill-red';
    const colorVal = score >= 80 ? 'var(--accent-green)' : score >= 60 ? 'var(--accent-amber)' : 'var(--accent-red)';
    html += '<div class="pillar-score-card">';
    html += '<div class="pillar-score-header">';
    html += '<span class="pillar-score-name">' + pillar.name + '</span>';
    html += '<span class="pillar-score-value" style="color: ' + colorVal + '">' + score + '%</span>';
    html += '</div>';
    html += '<div class="score-bar"><div class="score-bar-fill ' + fillClass + '" style="width: ' + score + '%"></div></div>';
    html += '</div>';
  });
  html += '</div>';
  
  // Gaps
  const gaps = [];
  all.forEach(q => {
    const ans = answers[q.id];
    if (ans === 'no' || ans === 'partial') {
      gaps.push({ pillar: q.pillarName, text: q.title, answer: ans });
    }
  });
  
  if (gaps.length > 0) {
    html += '<div class="gaps-section">';
    html += '<h3>Priority Gaps (' + gaps.length + ')</h3>';
    gaps.forEach(gap => {
      html += '<div class="gap-item">';
      html += '<div class="gap-pillar">' + gap.pillar + '</div>';
      html += '<div class="gap-text">' + gap.text + ' (' + (gap.answer === 'no' ? 'Not Implemented' : 'Partially Implemented') + ')</div>';
      html += '</div>';
    });
    html += '</div>';
  }
  
  // AWS Recommendations
  const allServices = new Set();
  gaps.forEach(gap => {
    const q = all.find(q => q.title === gap.text);
    if (q) {
      q.bestPractices.forEach(bp => bp.awsServices.forEach(s => allServices.add(s)));
    }
  });
  
  if (allServices.size > 0) {
    html += '<div class="aws-recommendations">';
    html += '<h3>Recommended AWS Services</h3>';
    [...allServices].forEach(s => {
      html += '<span class="rec-service">' + s + '</span>';
    });
    html += '</div>';
  }
  
  document.getElementById('report-body').innerHTML = html;
  document.getElementById('modal-overlay').style.display = 'flex';
}

function closeModal() {
  document.getElementById('modal-overlay').style.display = 'none';
}

function exportCSV() {
  const all = getAllQuestions();
  let csv = 'Pillar,Question,Answer,Notes\n';
  
  all.forEach(q => {
    const ans = answers[q.id] || 'Not Answered';
    const note = (notes[q.id] || '').replace(/,/g, ';');
    csv += '"' + q.pillarName + '","' + q.title + '","' + ans + '","' + note + '"\n';
  });
  
  const blob = new Blob([csv], { type: 'text/csv' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'mindforge-assessment-' + new Date().toISOString().split('T')[0] + '.csv';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function copySummary() {
  const overall = calculateOverallScore();
  const posture = getPostureLabel(overall);
  
  let summary = 'MAS MindForge Assessment Summary\n';
  summary += 'Date: ' + new Date().toLocaleDateString() + '\n';
  summary += 'Overall Score: ' + overall + '% (' + posture.label + ')\n\n';
  summary += 'Domain Scores:\n';
  PILLARS.forEach((pillar, index) => {
    summary += '- ' + pillar.name + ': ' + calculatePillarScore(index) + '%\n';
  });
  
  navigator.clipboard.writeText(summary).then(() => {
    alert('Summary copied to clipboard!');
  }).catch(err => {
    console.error('Copy failed:', err);
  });
}

window.MindForgeLens = {
  answers: () => answers,
  calculateOverallScore,
  calculatePillarScore,
  getPostureLabel
};
