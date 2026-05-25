import json
import os
import subprocess

PROJECT_DIR = os.path.expanduser("~/.openclaw/workspace/unofficial-wellarchitected-mas-mindforge-lens")
os.chdir(PROJECT_DIR)

# ============ DATA MODEL ============

PILLARS = [
    {
        "id": "oversight",
        "name": "AI Oversight",
        "description": "Governance scope, accountability, and oversight structures",
        "questions": [
            {
                "id": "Q1.1",
                "title": "Scope and Application",
                "text": "Is AI governance scope formally defined and operationalized across all AI systems?",
                "bestPractices": [
                    {"text": "AI governance scope is formally defined and documented", "awsServices": ["AWS Organizations", "AWS Config", "AWS Audit Manager"]},
                    {"text": "AI use cases are inventoried and classified by risk tier", "awsServices": ["AWS Config", "Amazon SageMaker Model Registry", "AWS Resource Explorer"]},
                    {"text": "Distinction between traditional AI, GenAI, and agentic AI is operationalized", "awsServices": ["AWS Config Rules", "Amazon Bedrock", "Amazon SageMaker"]}
                ],
                "improvementPlan": "Establish a formal AI governance charter that defines scope, creates an inventory of all AI systems, and operationalizes distinctions between AI types. Use AWS Config to track AI resources and AWS Audit Manager to document governance scope."
            },
            {
                "id": "Q1.2",
                "title": "Responsibilities for AI Oversight",
                "text": "Are AI oversight responsibilities clearly assigned across the three lines of defence?",
                "bestPractices": [
                    {"text": "Board or equivalent body has AI oversight accountability", "awsServices": ["AWS IAM", "Amazon QuickSight", "AWS Audit Manager"]},
                    {"text": "Three Lines of Defence model is applied to AI risk", "awsServices": ["AWS IAM", "AWS Organizations", "Amazon CloudWatch"]},
                    {"text": "AI ethics or risk committee is established", "awsServices": ["AWS IAM", "Amazon Chime", "AWS Systems Manager"]}
                ],
                "improvementPlan": "Establish clear accountability for AI governance by assigning board-level oversight, implementing the Three Lines of Defence model, and creating an AI ethics committee. Use AWS IAM for role-based access and Amazon QuickSight for governance dashboards."
            }
        ]
    },
    {
        "id": "risk",
        "name": "AI Risk Management",
        "description": "Policies, enterprise risk, third-party, use case, and inventory",
        "questions": [
            {
                "id": "Q2.1",
                "title": "AI-Related Policies and Standards",
                "text": "Are AI-related policies, procedures, and standards documented and approved?",
                "bestPractices": [
                    {"text": "AI policy framework is formally approved and communicated", "awsServices": ["AWS Audit Manager", "AWS Config", "AWS Security Hub"]},
                    {"text": "Model risk management standards are defined", "awsServices": ["Amazon SageMaker Model Cards", "Amazon SageMaker Model Monitor", "AWS CloudTrail"]},
                    {"text": "Data governance standards cover AI training and inference data", "awsServices": ["Amazon Macie", "AWS Glue", "Amazon S3"]}
                ],
                "improvementPlan": "Develop and approve a comprehensive AI policy framework that covers model risk management and data governance. Use AWS Audit Manager for policy documentation and Amazon SageMaker Model Cards for model governance."
            },
            {
                "id": "Q2.2",
                "title": "Organisation-Level Risk Management",
                "text": "Is AI risk integrated into the enterprise risk management framework?",
                "bestPractices": [
                    {"text": "AI risk is integrated into enterprise risk taxonomy", "awsServices": ["Amazon SageMaker Model Cards", "AWS Trusted Advisor", "AWS Cost Explorer"]},
                    {"text": "Materiality scoring for AI use cases is operationalized", "awsServices": ["Amazon SageMaker Clarify", "Amazon CloudWatch", "AWS X-Ray"]},
                    {"text": "AI risk appetite statement is defined and approved", "awsServices": ["AWS Audit Manager", "Amazon QuickSight", "AWS Config"]}
                ],
                "improvementPlan": "Integrate AI risk into the enterprise risk taxonomy with materiality scoring and a defined risk appetite statement. Use SageMaker Clarify for bias detection and Amazon QuickSight for risk dashboards."
            },
            {
                "id": "Q2.3",
                "title": "Third Party AI Risk Management",
                "text": "Are risks from third-party AI services, models, and data providers managed?",
                "bestPractices": [
                    {"text": "Third-party AI vendor assessment framework exists", "awsServices": ["AWS Artifact", "AWS Marketplace", "AWS PrivateLink"]},
                    {"text": "Cloud AI service agreements include risk provisions", "awsServices": ["AWS Artifact", "AWS Certificate Manager", "AWS PrivateLink"]}
                ],
                "improvementPlan": "Implement a third-party AI vendor assessment framework and ensure cloud AI service agreements include risk provisions. Use AWS Artifact for compliance documentation and AWS PrivateLink for secure connectivity."
            },
            {
                "id": "Q2.4",
                "title": "Use Case-Level AI Risk Management",
                "text": "Is AI risk assessed and managed at the individual use case level?",
                "bestPractices": [
                    {"text": "AI risk assessments are conducted per use case", "awsServices": ["Amazon SageMaker Model Cards", "Amazon Bedrock Guardrails", "Amazon Macie"]},
                    {"text": "AI Cards or equivalent risk documents are maintained", "awsServices": ["Amazon SageMaker Model Cards", "AWS Systems Manager", "Amazon S3"]},
                    {"text": "Use case risk ratings are reviewed periodically", "awsServices": ["Amazon SageMaker Model Monitor", "Amazon CloudWatch", "AWS Lambda"]}
                ],
                "improvementPlan": "Conduct per-use-case AI risk assessments and maintain AI Cards for each system. Use SageMaker Model Cards for documentation and SageMaker Model Monitor for ongoing validation."
            },
            {
                "id": "Q2.5",
                "title": "AI Inventory Capabilities",
                "text": "Is a comprehensive inventory of AI assets maintained with appropriate metadata?",
                "bestPractices": [
                    {"text": "AI inventory system is implemented and maintained", "awsServices": ["AWS Config", "Amazon SageMaker Model Registry", "AWS Resource Explorer"]},
                    {"text": "Inventory captures model lineage, ownership, and risk tier", "awsServices": ["Amazon SageMaker Model Registry", "AWS Glue", "Amazon DynamoDB"]}
                ],
                "improvementPlan": "Implement an AI inventory system that captures model lineage, ownership, and risk tier. Use AWS Config for resource tracking and SageMaker Model Registry for model versioning."
            }
        ]
    },
    {
        "id": "lifecycle",
        "name": "AI Lifecycle Management",
        "description": "Context, data, build, deploy, and monitoring",
        "questions": [
            {
                "id": "Q3.1",
                "title": "Use Case Context and Design",
                "text": "Is use case context and design defined before development begins?",
                "bestPractices": [
                    {"text": "Business problem and success metrics are defined", "awsServices": ["Amazon SageMaker", "Amazon Bedrock", "AWS Systems Manager"]},
                    {"text": "Fairness and bias assessment is conducted at design stage", "awsServices": ["Amazon SageMaker Clarify", "Amazon Bedrock Guardrails", "AWS Lambda"]}
                ],
                "improvementPlan": "Define business problems and success metrics before development. Conduct fairness and bias assessments at the design stage using SageMaker Clarify and Bedrock Guardrails."
            },
            {
                "id": "Q3.2",
                "title": "Data Acquisition and Processing",
                "text": "Is data quality, provenance, and privacy managed throughout the lifecycle?",
                "bestPractices": [
                    {"text": "Data lineage and provenance are tracked", "awsServices": ["AWS Glue", "Amazon S3", "AWS Lake Formation"]},
                    {"text": "Data quality assessment processes are in place", "awsServices": ["AWS Glue DataBrew", "Amazon CloudWatch", "AWS Lambda"]},
                    {"text": "Privacy and consent requirements are addressed", "awsServices": ["Amazon Macie", "AWS KMS", "Amazon S3"]}
                ],
                "improvementPlan": "Implement data lineage tracking, quality assessments, and privacy controls. Use AWS Glue for data cataloging, Amazon Macie for privacy scanning, and AWS KMS for encryption."
            },
            {
                "id": "Q3.3",
                "title": "Onboarding, Build, and Review",
                "text": "Are rigorous development practices including validation and independent review applied?",
                "bestPractices": [
                    {"text": "Model validation and testing protocols are defined", "awsServices": ["Amazon SageMaker Clarify", "Amazon SageMaker Model Monitor", "AWS CodePipeline"]},
                    {"text": "Independent model review or validation is conducted", "awsServices": ["Amazon SageMaker Model Cards", "AWS CodeBuild", "Amazon CloudWatch"]},
                    {"text": "Documentation of model assumptions and limitations exists", "awsServices": ["Amazon SageMaker Model Cards", "AWS Systems Manager", "Amazon S3"]}
                ],
                "improvementPlan": "Define model validation protocols, conduct independent reviews, and document assumptions. Use SageMaker Clarify for bias testing and SageMaker Model Cards for documentation."
            },
            {
                "id": "Q3.4",
                "title": "Deployment",
                "text": "Is the transition to production managed with appropriate controls and approvals?",
                "bestPractices": [
                    {"text": "Deployment approval process includes risk sign-off", "awsServices": ["AWS CloudFormation", "AWS Systems Manager", "Amazon SNS"]},
                    {"text": "Rollback and incident response plans exist", "awsServices": ["AWS Lambda", "Amazon CloudWatch", "AWS CloudFormation"]}
                ],
                "improvementPlan": "Implement deployment approval workflows with risk sign-off and create rollback plans. Use AWS CloudFormation for infrastructure as code and Amazon CloudWatch for monitoring."
            },
            {
                "id": "Q3.5",
                "title": "Usage, Monitoring, and Change Management",
                "text": "Is AI performance continuously monitored with drift detection and change management?",
                "bestPractices": [
                    {"text": "Production monitoring includes performance and fairness metrics", "awsServices": ["Amazon CloudWatch", "Amazon SageMaker Model Monitor", "AWS X-Ray"]},
                    {"text": "Model drift detection is operationalized", "awsServices": ["Amazon SageMaker Model Monitor", "Amazon CloudWatch", "AWS Lambda"]},
                    {"text": "Change management process covers model updates", "awsServices": ["AWS CodePipeline", "Amazon SageMaker Pipelines", "AWS Systems Manager"]}
                ],
                "improvementPlan": "Operationalize production monitoring with drift detection and implement change management for model updates. Use SageMaker Model Monitor for drift detection and AWS CodePipeline for CI/CD."
            }
        ]
    },
    {
        "id": "enablers",
        "name": "Enablers",
        "description": "Skills, knowledge, culture, and infrastructure",
        "questions": [
            {
                "id": "Q4.1",
                "title": "Skills, Knowledge, and Culture",
                "text": "Is AI governance supported by appropriate skills, knowledge, and risk-aware culture?",
                "bestPractices": [
                    {"text": "AI risk training is provided to relevant staff", "awsServices": ["AWS Training and Certification", "Amazon QuickSight", "Amazon Chime"]},
                    {"text": "AI literacy programme covers business and technical staff", "awsServices": ["AWS Training and Certification", "Amazon QuickSight", "AWS Systems Manager"]}
                ],
                "improvementPlan": "Develop AI risk training programs and AI literacy initiatives for all staff. Use AWS Training and Certification for technical training and Amazon QuickSight for data literacy."
            },
            {
                "id": "Q4.2",
                "title": "AI Infrastructure",
                "text": "Is the underlying AI infrastructure secure, resilient, and adequate?",
                "bestPractices": [
                    {"text": "AI development environment is secured and segregated", "awsServices": ["Amazon VPC", "AWS KMS", "AWS Secrets Manager"]},
                    {"text": "Compute and storage resources meet AI workload requirements", "awsServices": ["Amazon EC2", "Amazon S3", "AWS Auto Scaling"]},
                    {"text": "Disaster recovery plans cover AI systems", "awsServices": ["AWS Backup", "Amazon S3", "AWS CloudFormation"]}
                ],
                "improvementPlan": "Secure and segregate AI development environments, ensure adequate compute and storage, and implement disaster recovery. Use Amazon VPC for network isolation and AWS KMS for encryption."
            }
        ]
    }
]

# ============ HTML GENERATOR ============

def generate_html():
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Interactive Well-Architected Questionnaire for MAS Project MindForge AI Risk Management with AWS native service recommendations">
<meta property="og:title" content="MAS MindForge Well-Architected Lens">
<meta property="og:description" content="AWS native service recommendations for MAS AI Risk Management framework">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none';">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>MAS MindForge Well-Architected Lens</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="app-container">
  <header class="app-header">
    <div class="header-left">
      <h1>MAS MindForge Well-Architected Lens</h1>
      <p class="subtitle">AI Risk Management Assessment with AWS Native Service Recommendations</p>
    </div>
    <div class="header-right">
      <div class="score-display" id="score-display">
        <span class="score-label">Overall Maturity</span>
        <span class="score-value" id="overall-score">--</span>
      </div>
      <div class="progress-display">
        <span id="progress-text">0/14</span>
      </div>
    </div>
  </header>

  <div class="main-layout">
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <h3>Pillars</h3>
      </div>
      <div class="pillar-list" id="pillar-list"></div>
    </aside>

    <main class="content-area" id="content-area">
      <div class="question-card" id="question-card">
        <div class="question-header">
          <span class="pillar-badge" id="current-pillar-badge">Pillar</span>
          <span class="question-number" id="question-number">Question 1 of 14</span>
        </div>
        <h2 class="question-title" id="question-title">Loading...</h2>
        <p class="question-description" id="question-description"></p>

        <div class="answer-section">
          <h4>Select your current state:</h4>
          <div class="answer-buttons" id="answer-buttons">
            <button class="answer-btn yes" data-value="yes" tabindex="0">
              <span class="answer-icon">Yes</span>
              <span class="answer-label">Implemented</span>
            </button>
            <button class="answer-btn partial" data-value="partial" tabindex="0">
              <span class="answer-icon">Partial</span>
              <span class="answer-label">Partially Implemented</span>
            </button>
            <button class="answer-btn no" data-value="no" tabindex="0">
              <span class="answer-icon">No</span>
              <span class="answer-label">Not Implemented</span>
            </button>
            <button class="answer-btn na" data-value="na" tabindex="0">
              <span class="answer-icon">N/A</span>
              <span class="answer-label">Not Applicable</span>
            </button>
          </div>
        </div>

        <div class="best-practices-section" id="best-practices-section">
          <h4>Best Practices</h4>
          <ul class="best-practices-list" id="best-practices-list"></ul>
        </div>

        <div class="aws-services-section" id="aws-services-section">
          <h4>Recommended AWS Services</h4>
          <div class="aws-services-grid" id="aws-services-grid"></div>
        </div>

        <div class="improvement-section" id="improvement-section">
          <h4>Improvement Plan</h4>
          <p class="improvement-text" id="improvement-text"></p>
        </div>

        <div class="notes-section">
          <h4>Notes</h4>
          <textarea class="notes-textarea" id="notes-textarea" placeholder="Add notes about this question..."></textarea>
        </div>
      </div>

      <div class="navigation-bar">
        <button class="nav-btn prev" id="prev-btn" tabindex="0">Previous</button>
        <button class="nav-btn next" id="next-btn" tabindex="0">Next</button>
        <button class="nav-btn report" id="report-btn" tabindex="0" style="display:none;">Generate Report</button>
      </div>
    </main>
  </div>

  <div class="modal-overlay" id="modal-overlay" style="display:none;">
    <div class="modal-content">
      <div class="modal-header">
        <h2>Assessment Report</h2>
        <button class="modal-close" id="modal-close">&times;</button>
      </div>
      <div class="modal-body" id="report-body"></div>
      <div class="modal-footer">
        <button class="secondary-btn" id="export-csv-btn">Export CSV</button>
        <button class="secondary-btn" id="copy-summary-btn">Copy Summary</button>
        <button class="primary-btn" id="close-modal-btn">Close</button>
      </div>
    </div>
  </div>

  <footer class="app-footer">
    <p>Based on MAS Project MindForge AI Risk Management Operationalisation Handbook (January 2026)</p>
    <p class="version">v1.1 | AWS Well-Architected Style Questionnaire</p>
  </footer>
</div>
<script src="app.js"></script>
</body>
</html>'''
    return html

# ============ CSS GENERATOR ============

def generate_css():
    css = '''/* MAS MindForge Well-Architected Lens - Dark Theme */

:root {
  --bg-primary: #0f172a;
  --bg-secondary: #1e293b;
  --bg-card: #1e293b;
  --bg-hover: #334155;
  --text-primary: #f1f5f9;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  --accent-blue: #3b82f6;
  --accent-green: #22c55e;
  --accent-amber: #f59e0b;
  --accent-red: #ef4444;
  --accent-purple: #8b5cf6;
  --accent-cyan: #06b6d4;
  --border-color: #334155;
  --success: #22c55e;
  --warning: #f59e0b;
  --danger: #ef4444;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
  background: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
  min-height: 100vh;
}

.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* Header */
.app-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 30px;
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border-color);
}

.header-left h1 {
  font-size: 1.5rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.subtitle {
  color: var(--text-secondary);
  font-size: 0.85rem;
  margin-top: 4px;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 20px;
}

.score-display {
  text-align: center;
  padding: 10px 20px;
  background: var(--bg-primary);
  border-radius: 8px;
  border: 1px solid var(--border-color);
}

.score-label {
  display: block;
  font-size: 0.75rem;
  color: var(--text-muted);
  text-transform: uppercase;
}

.score-value {
  display: block;
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--accent-blue);
}

.progress-display {
  font-size: 0.9rem;
  color: var(--text-secondary);
}

/* Layout */
.main-layout {
  display: flex;
  flex: 1;
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
  padding: 20px;
  gap: 20px;
}

/* Sidebar */
.sidebar {
  width: 280px;
  flex-shrink: 0;
  background: var(--bg-secondary);
  border-radius: 12px;
  border: 1px solid var(--border-color);
  overflow: hidden;
}

.sidebar-header {
  padding: 15px 20px;
  border-bottom: 1px solid var(--border-color);
}

.sidebar-header h3 {
  font-size: 0.9rem;
  text-transform: uppercase;
  color: var(--text-muted);
  letter-spacing: 1px;
}

.pillar-list {
  padding: 10px;
}

.pillar-item {
  margin-bottom: 8px;
  border-radius: 8px;
  overflow: hidden;
}

.pillar-header {
  padding: 12px 15px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background 0.2s;
  border-radius: 8px;
}

.pillar-header:hover {
  background: var(--bg-hover);
}

.pillar-header.active {
  background: rgba(59, 130, 246, 0.15);
  border-left: 3px solid var(--accent-blue);
}

.pillar-name {
  font-weight: 600;
  font-size: 0.9rem;
}

.pillar-score {
  font-size: 0.8rem;
  color: var(--text-muted);
}

.question-list {
  padding: 0 10px 10px;
}

.question-item {
  padding: 8px 12px;
  margin: 2px 0;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.85rem;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: background 0.2s;
}

.question-item:hover {
  background: var(--bg-hover);
}

.question-item.active {
  background: rgba(59, 130, 246, 0.2);
  color: var(--accent-blue);
}

.question-item.answered-yes { border-left: 3px solid var(--accent-green); }
.question-item.answered-partial { border-left: 3px solid var(--accent-amber); }
.question-item.answered-no { border-left: 3px solid var(--accent-red); }
.question-item.answered-na { border-left: 3px solid var(--text-muted); }

/* Content Area */
.content-area {
  flex: 1;
  min-width: 0;
}

.question-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 30px;
  margin-bottom: 20px;
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid var(--border-color);
}

.pillar-badge {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  background: rgba(59, 130, 246, 0.2);
  color: var(--accent-blue);
}

.question-number {
  font-size: 0.85rem;
  color: var(--text-muted);
}

.question-title {
  font-size: 1.3rem;
  margin-bottom: 10px;
  color: var(--text-primary);
}

.question-description {
  color: var(--text-secondary);
  margin-bottom: 25px;
  font-size: 1rem;
  line-height: 1.6;
}

/* Answer Buttons */
.answer-section {
  margin-bottom: 25px;
}

.answer-section h4 {
  font-size: 0.9rem;
  color: var(--text-secondary);
  margin-bottom: 12px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.answer-buttons {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.answer-btn {
  padding: 15px;
  border: 2px solid var(--border-color);
  border-radius: 8px;
  background: var(--bg-primary);
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
}

.answer-btn:hover {
  border-color: var(--accent-blue);
  color: var(--text-primary);
  transform: translateY(-2px);
}

.answer-btn.selected-yes {
  border-color: var(--accent-green);
  background: rgba(34, 197, 94, 0.15);
  color: var(--accent-green);
}

.answer-btn.selected-partial {
  border-color: var(--accent-amber);
  background: rgba(245, 158, 11, 0.15);
  color: var(--accent-amber);
}

.answer-btn.selected-no {
  border-color: var(--accent-red);
  background: rgba(239, 68, 68, 0.15);
  color: var(--accent-red);
}

.answer-btn.selected-na {
  border-color: var(--text-muted);
  background: rgba(100, 116, 139, 0.15);
  color: var(--text-muted);
}

.answer-icon {
  font-size: 1.1rem;
  font-weight: 700;
}

.answer-label {
  font-size: 0.8rem;
}

/* Sections */
.best-practices-section,
.aws-services-section,
.improvement-section,
.notes-section {
  margin-top: 25px;
  padding-top: 25px;
  border-top: 1px solid var(--border-color);
}

.best-practices-section h4,
.aws-services-section h4,
.improvement-section h4,
.notes-section h4 {
  font-size: 0.9rem;
  color: var(--text-secondary);
  margin-bottom: 12px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.best-practices-list {
  list-style: none;
}

.best-practices-list li {
  padding: 10px 0;
  border-bottom: 1px solid var(--border-color);
  color: var(--text-primary);
  display: flex;
  align-items: flex-start;
  gap: 10px;
}

.best-practices-list li::before {
  content: '';
  display: inline-block;
  width: 6px;
  height: 6px;
  background: var(--accent-blue);
  border-radius: 50%;
  margin-top: 8px;
  flex-shrink: 0;
}

.best-practices-list li:last-child {
  border-bottom: none;
}

.aws-services-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.aws-service-badge {
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
  background: rgba(6, 182, 212, 0.15);
  color: var(--accent-cyan);
  border: 1px solid rgba(6, 182, 212, 0.3);
}

.improvement-text {
  color: var(--text-secondary);
  line-height: 1.6;
  padding: 15px;
  background: var(--bg-primary);
  border-radius: 8px;
  border-left: 3px solid var(--accent-amber);
}

.notes-textarea {
  width: 100%;
  min-height: 80px;
  padding: 12px;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  background: var(--bg-primary);
  color: var(--text-primary);
  font-family: inherit;
  font-size: 0.9rem;
  resize: vertical;
}

.notes-textarea:focus {
  outline: none;
  border-color: var(--accent-blue);
}

/* Navigation */
.navigation-bar {
  display: flex;
  justify-content: space-between;
  gap: 12px;
}

.nav-btn {
  padding: 12px 24px;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  background: var(--bg-secondary);
  color: var(--text-secondary);
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.nav-btn:hover {
  border-color: var(--accent-blue);
  color: var(--text-primary);
  background: var(--bg-hover);
}

.nav-btn.report {
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
  color: white;
  border: none;
  font-weight: 600;
}

.nav-btn.report:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 20px rgba(59, 130, 246, 0.3);
}

.nav-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
}

.modal-content {
  background: var(--bg-secondary);
  border-radius: 12px;
  border: 1px solid var(--border-color);
  max-width: 900px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 30px;
  border-bottom: 1px solid var(--border-color);
}

.modal-header h2 {
  font-size: 1.3rem;
}

.modal-close {
  background: none;
  border: none;
  color: var(--text-secondary);
  font-size: 1.5rem;
  cursor: pointer;
  padding: 0;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  transition: background 0.2s;
}

.modal-close:hover {
  background: var(--bg-hover);
  color: var(--text-primary);
}

.modal-body {
  padding: 30px;
}

.modal-footer {
  display: flex;
  gap: 12px;
  padding: 20px 30px;
  border-top: 1px solid var(--border-color);
  justify-content: flex-end;
}

/* Report Styles */
.report-summary {
  text-align: center;
  margin-bottom: 30px;
  padding: 30px;
  background: var(--bg-primary);
  border-radius: 12px;
}

.report-score {
  font-size: 3rem;
  font-weight: 700;
  color: var(--accent-blue);
}

.report-label {
  font-size: 1rem;
  color: var(--text-secondary);
  margin-top: 10px;
}

.report-posture {
  display: inline-block;
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  margin-top: 15px;
}

.posture-strong { background: rgba(34, 197, 94, 0.2); color: var(--accent-green); }
.posture-moderate { background: rgba(245, 158, 11, 0.2); color: var(--accent-amber); }
.posture-developing { background: rgba(239, 68, 68, 0.2); color: var(--accent-red); }
.posture-critical { background: rgba(239, 68, 68, 0.3); color: var(--accent-red); }

.pillar-scores-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 15px;
  margin-bottom: 30px;
}

.pillar-score-card {
  padding: 20px;
  background: var(--bg-primary);
  border-radius: 8px;
  border: 1px solid var(--border-color);
}

.pillar-score-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.pillar-score-name {
  font-weight: 600;
}

.pillar-score-value {
  font-size: 1.2rem;
  font-weight: 700;
}

.score-bar {
  height: 8px;
  background: var(--bg-secondary);
  border-radius: 4px;
  overflow: hidden;
}

.score-bar-fill {
  height: 100%;
  border-radius: 4px;
  transition: width 0.5s ease;
}

.fill-green { background: var(--accent-green); }
.fill-amber { background: var(--accent-amber); }
.fill-red { background: var(--accent-red); }

.gaps-section {
  margin-top: 30px;
}

.gaps-section h3 {
  margin-bottom: 15px;
  font-size: 1.1rem;
}

.gap-item {
  padding: 12px;
  background: var(--bg-primary);
  border-radius: 8px;
  margin-bottom: 8px;
  border-left: 3px solid var(--accent-red);
}

.gap-pillar {
  font-size: 0.8rem;
  color: var(--text-muted);
  text-transform: uppercase;
}

.gap-text {
  color: var(--text-primary);
  margin-top: 4px;
}

.aws-recommendations {
  margin-top: 30px;
}

.aws-recommendations h3 {
  margin-bottom: 15px;
  font-size: 1.1rem;
}

.rec-service {
  display: inline-block;
  padding: 8px 14px;
  margin: 4px;
  border-radius: 20px;
  font-size: 0.85rem;
  background: rgba(6, 182, 212, 0.15);
  color: var(--accent-cyan);
  border: 1px solid rgba(6, 182, 212, 0.3);
}

/* Buttons */
.primary-btn {
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
  color: white;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.primary-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 20px rgba(59, 130, 246, 0.3);
}

.secondary-btn {
  padding: 10px 20px;
  border: 1px solid var(--border-color);
  border-radius: 6px;
  background: var(--bg-primary);
  color: var(--text-secondary);
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.secondary-btn:hover {
  border-color: var(--accent-blue);
  color: var(--text-primary);
}

/* Footer */
.app-footer {
  text-align: center;
  padding: 20px;
  border-top: 1px solid var(--border-color);
  color: var(--text-muted);
  font-size: 0.8rem;
}

.app-footer .version {
  margin-top: 5px;
}

/* Responsive */
@media (max-width: 1024px) {
  .main-layout {
    flex-direction: column;
  }
  
  .sidebar {
    width: 100%;
  }
  
  .answer-buttons {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .pillar-scores-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .app-header {
    flex-direction: column;
    gap: 15px;
  }
  
  .answer-buttons {
    grid-template-columns: 1fr;
  }
  
  .question-card {
    padding: 20px;
  }
}
'''
    return css

# ============ JS GENERATOR ============

def generate_js():
    # Serialize the data model to JSON for embedding
    pillars_json = json.dumps(PILLARS, indent=2)
    
    js = f'''// MAS MindForge Well-Architected Lens - Interactive Questionnaire
// v1.1 with AWS Native Service Recommendations

'use strict';

const PILLARS = {pillars_json};

const STORAGE_KEY = 'mindforge_wa_v1';

let answers = {{}};
let notes = {{}};
let currentPillar = 0;
let currentQuestion = 0;

// Initialize
document.addEventListener('DOMContentLoaded', function() {{
  loadState();
  renderSidebar();
  renderQuestion();
  setupEventListeners();
  updateProgress();
}});

function loadState() {{
  try {{
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {{
      const data = JSON.parse(stored);
      answers = data.answers || {{}};
      notes = data.notes || {{}};
    }}
  }} catch (e) {{
    console.warn('Failed to load state:', e);
  }}
}}

function saveState() {{
  try {{
    localStorage.setItem(STORAGE_KEY, JSON.stringify({{ answers, notes }}));
  }} catch (e) {{
    console.warn('Failed to save state:', e);
  }}
}}

function getAllQuestions() {{
  const questions = [];
  PILLARS.forEach((pillar, pIndex) => {{
    pillar.questions.forEach((q, qIndex) => {{
      questions.push({{
        ...q,
        pillarIndex: pIndex,
        questionIndex: qIndex,
        pillarName: pillar.name,
        pillarId: pillar.id
      }});
    }});
  }});
  return questions;
}}

function getCurrentQuestion() {{
  const all = getAllQuestions();
  return all[currentQuestion] || null;
}}

function renderSidebar() {{
  const container = document.getElementById('pillar-list');
  if (!container) return;
  
  let html = '';
  PILLARS.forEach((pillar, pIndex) => {{
    const isActive = pIndex === currentPillar;
    html += `<div class="pillar-item">`;
    html += `<div class="pillar-header ${{isActive ? 'active' : ''}}" data-pillar="${{pIndex}}">`;
    html += `<span class="pillar-name">${{pillar.name}}</span>`;
    html += `<span class="pillar-score">${{pillar.questions.length}} Qs</span>`;
    html += `</div>`;
    
    if (isActive) {{
      html += `<div class="question-list">`;
      pillar.questions.forEach((q, qIndex) => {{
        const globalIndex = PILLARS.slice(0, pIndex).reduce((sum, p) => sum + p.questions.length, 0) + qIndex;
        const answer = answers[q.id];
        const isCurrent = globalIndex === currentQuestion;
        html += `<div class="question-item ${{isCurrent ? 'active' : ''}} answered-${{answer || ''}}" data-index="${{globalIndex}}">`;
        html += `<span>${{q.id}}</span>`;
        html += `</div>`;
      }});
      html += `</div>`;
    }}
    
    html += `</div>`;
  }});
  
  container.innerHTML = html;
  
  // Add click handlers
  container.querySelectorAll('.pillar-header').forEach(header => {{
    header.addEventListener('click', () => {{
      currentPillar = parseInt(header.dataset.pillar);
      const all = getAllQuestions();
      const firstInPillar = all.findIndex(q => q.pillarIndex === currentPillar);
      if (firstInPillar >= 0) {{
        currentQuestion = firstInPillar;
        renderSidebar();
        renderQuestion();
      }}
    }});
  }});
  
  container.querySelectorAll('.question-item').forEach(item => {{
    item.addEventListener('click', () => {{
      currentQuestion = parseInt(item.dataset.index);
      const q = getCurrentQuestion();
      if (q) {{
        currentPillar = q.pillarIndex;
      }}
      renderSidebar();
      renderQuestion();
    }});
  }});
}}

function renderQuestion() {{
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
  if (number) number.textContent = `Question ${{currentQuestion + 1}} of ${{getAllQuestions().length}}`;
  if (title) title.textContent = q.title;
  if (desc) desc.textContent = q.text;
  
  // Best practices
  if (practicesList) {{
    practicesList.innerHTML = q.bestPractices.map(bp => `<li>${{bp.text}}</li>`).join('');
  }}
  
  // AWS Services
  if (servicesGrid) {{
    const allServices = q.bestPractices.flatMap(bp => bp.awsServices);
    const unique = [...new Set(allServices)];
    servicesGrid.innerHTML = unique.map(s => `<span class="aws-service-badge">${{s}}</span>`).join('');
  }}
  
  // Improvement plan
  if (improvementText) {{
    improvementText.textContent = q.improvementPlan;
  }}
  
  // Notes
  if (notesArea) {{
    notesArea.value = notes[q.id] || '';
  }}
  
  // Answer buttons
  document.querySelectorAll('.answer-btn').forEach(btn => {{
    btn.className = 'answer-btn';
    const val = btn.dataset.value;
    if (answers[q.id] === val) {{
      btn.classList.add('selected-' + val);
    }}
  }});
  
  // Navigation buttons
  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');
  const reportBtn = document.getElementById('report-btn');
  
  if (prevBtn) prevBtn.disabled = currentQuestion === 0;
  if (nextBtn) {{
    const all = getAllQuestions();
    nextBtn.style.display = currentQuestion === all.length - 1 ? 'none' : 'inline-block';
  }}
  if (reportBtn) {{
    const all = getAllQuestions();
    const answered = Object.keys(answers).length;
    reportBtn.style.display = answered >= all.length ? 'inline-block' : 'none';
  }}
}}

function setupEventListeners() {{
  // Answer buttons
  document.querySelectorAll('.answer-btn').forEach(btn => {{
    btn.addEventListener('click', () => {{
      const q = getCurrentQuestion();
      if (!q) return;
      
      answers[q.id] = btn.dataset.value;
      saveState();
      
      document.querySelectorAll('.answer-btn').forEach(b => b.className = 'answer-btn');
      btn.classList.add('selected-' + btn.dataset.value);
      
      updateProgress();
      renderSidebar();
      
      // Auto-advance after short delay
      setTimeout(() => {{
        const all = getAllQuestions();
        if (currentQuestion < all.length - 1) {{
          currentQuestion++;
          const nextQ = getCurrentQuestion();
          if (nextQ) currentPillar = nextQ.pillarIndex;
          renderSidebar();
          renderQuestion();
        }}
      }}, 300);
    }});
  }});
  
  // Notes
  const notesArea = document.getElementById('notes-textarea');
  if (notesArea) {{
    notesArea.addEventListener('input', () => {{
      const q = getCurrentQuestion();
      if (q) {{
        notes[q.id] = notesArea.value;
        saveState();
      }}
    }});
  }}
  
  // Navigation
  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');
  const reportBtn = document.getElementById('report-btn');
  
  if (prevBtn) {{
    prevBtn.addEventListener('click', () => {{
      if (currentQuestion > 0) {{
        currentQuestion--;
        const q = getCurrentQuestion();
        if (q) currentPillar = q.pillarIndex;
        renderSidebar();
        renderQuestion();
      }}
    }});
  }}
  
  if (nextBtn) {{
    nextBtn.addEventListener('click', () => {{
      const all = getAllQuestions();
      if (currentQuestion < all.length - 1) {{
        currentQuestion++;
        const q = getCurrentQuestion();
        if (q) currentPillar = q.pillarIndex;
        renderSidebar();
        renderQuestion();
      }}
    }});
  }}
  
  if (reportBtn) {{
    reportBtn.addEventListener('click', generateReport);
  }}
  
  // Modal
  const modalClose = document.getElementById('modal-close');
  const closeModalBtn = document.getElementById('close-modal-btn');
  const overlay = document.getElementById('modal-overlay');
  
  if (modalClose) modalClose.addEventListener('click', closeModal);
  if (closeModalBtn) closeModalBtn.addEventListener('click', closeModal);
  if (overlay) overlay.addEventListener('click', (e) => {{
    if (e.target === overlay) closeModal();
  }});
  
  // Export buttons
  const exportCsvBtn = document.getElementById('export-csv-btn');
  const copySummaryBtn = document.getElementById('copy-summary-btn');
  
  if (exportCsvBtn) exportCsvBtn.addEventListener('click', exportCSV);
  if (copySummaryBtn) copySummaryBtn.addEventListener('click', copySummary);
  
  // Keyboard navigation
  document.addEventListener('keydown', (e) => {{
    if (e.key === 'ArrowRight') {{
      const all = getAllQuestions();
      if (currentQuestion < all.length - 1) {{
        currentQuestion++;
        const q = getCurrentQuestion();
        if (q) currentPillar = q.pillarIndex;
        renderSidebar();
        renderQuestion();
      }}
    }} else if (e.key === 'ArrowLeft') {{
      if (currentQuestion > 0) {{
        currentQuestion--;
        const q = getCurrentQuestion();
        if (q) currentPillar = q.pillarIndex;
        renderSidebar();
        renderQuestion();
      }}
    }} else if (['1', '2', '3', '4'].includes(e.key)) {{
      const values = ['yes', 'partial', 'no', 'na'];
      const btn = document.querySelector(`.answer-btn[data-value="${{values[parseInt(e.key) - 1]}}"]`);
      if (btn) btn.click();
    }}
  }});
}}

function updateProgress() {{
  const all = getAllQuestions();
  const answered = Object.keys(answers).length;
  const progressText = document.getElementById('progress-text');
  const scoreValue = document.getElementById('overall-score');
  
  if (progressText) progressText.textContent = `${{answered}}/${{all.length}}`;
  
  if (answered > 0) {{
    const score = calculateOverallScore();
    if (scoreValue) scoreValue.textContent = score + '%';
  }}
}}

function calculateOverallScore() {{
  const all = getAllQuestions();
  let total = 0;
  let count = 0;
  
  all.forEach(q => {{
    const ans = answers[q.id];
    if (ans && ans !== 'na') {{
      total += {{ 'yes': 3, 'partial': 2, 'no': 0 }}[ans] || 0;
      count++;
    }}
  }});
  
  if (count === 0) return 0;
  return Math.round((total / (count * 3)) * 100);
}}

function calculatePillarScore(pillarIndex) {{
  const pillar = PILLARS[pillarIndex];
  let total = 0;
  let count = 0;
  
  pillar.questions.forEach(q => {{
    const ans = answers[q.id];
    if (ans && ans !== 'na') {{
      total += {{ 'yes': 3, 'partial': 2, 'no': 0 }}[ans] || 0;
      count++;
    }}
  }});
  
  if (count === 0) return 0;
  return Math.round((total / (count * 3)) * 100);
}}

function getPostureLabel(score) {{
  if (score >= 80) return {{ label: 'Strong', class: 'posture-strong' }};
  if (score >= 60) return {{ label: 'Moderate', class: 'posture-moderate' }};
  if (score >= 40) return {{ label: 'Developing', class: 'posture-developing' }};
  return {{ label: 'Critical', class: 'posture-critical' }};
}}

function generateReport() {{
  const overall = calculateOverallScore();
  const posture = getPostureLabel(overall);
  const all = getAllQuestions();
  
  let html = '';
  
  // Summary
  html += `<div class="report-summary">`;
  html += `<div class="report-score">${{overall}}%</div>`;
  html += `<div class="report-label">Overall Maturity Score</div>`;
  html += `<div class="report-posture ${{posture.class}}">${{posture.label}} Posture</div>`;
  html += `</div>`;
  
  // Pillar scores
  html += `<h3>Domain Scores</h3>`;
  html += `<div class="pillar-scores-grid">`;
  PILLARS.forEach((pillar, index) => {{
    const score = calculatePillarScore(index);
    const fillClass = score >= 80 ? 'fill-green' : score >= 60 ? 'fill-amber' : 'fill-red';
    html += `<div class="pillar-score-card">`;
    html += `<div class="pillar-score-header">`;
    html += `<span class="pillar-score-name">${{pillar.name}}</span>`;
    html += `<span class="pillar-score-value" style="color: ${{score >= 80 ? 'var(--accent-green)' : score >= 60 ? 'var(--accent-amber)' : 'var(--accent-red)'}}">${{score}}%</span>`;
    html += `</div>`;
    html += `<div class="score-bar"><div class="score-bar-fill ${{fillClass}}" style="width: ${{score}}%"></div></div>`;
    html += `</div>`;
  }});
  html += `</div>`;
  
  // Gaps
  const gaps = [];
  all.forEach(q => {{
    const ans = answers[q.id];
    if (ans === 'no' || ans === 'partial') {{
      gaps.push({{ pillar: q.pillarName, text: q.title, answer: ans }});
    }}
  }});
  
  if (gaps.length > 0) {{
    html += `<div class="gaps-section">`;
    html += `<h3>Priority Gaps (${{gaps.length}})</h3>`;
    gaps.forEach(gap => {{
      html += `<div class="gap-item">`;
      html += `<div class="gap-pillar">${{gap.pillar}}</div>`;
      html += `<div class="gap-text">${{gap.text}} (${{gap.answer === 'no' ? 'Not Implemented' : 'Partially Implemented'}})</div>`;
      html += `</div>`;
    }});
    html += `</div>`;
  }}
  
  // AWS Recommendations
  const allServices = new Set();
  gaps.forEach(gap => {{
    const q = all.find(q => q.title === gap.text);
    if (q) {{
      q.bestPractices.forEach(bp => bp.awsServices.forEach(s => allServices.add(s)));
    }}
  }});
  
  if (allServices.size > 0) {{
    html += `<div class="aws-recommendations">`;
    html += `<h3>Recommended AWS Services</h3>`;
    [...allServices].forEach(s => {{
      html += `<span class="rec-service">${{s}}</span>`;
    }});
    html += `</div>`;
  }}
  
  document.getElementById('report-body').innerHTML = html;
  document.getElementById('modal-overlay').style.display = 'flex';
}}

function closeModal() {{
  document.getElementById('modal-overlay').style.display = 'none';
}}

function exportCSV() {{
  const all = getAllQuestions();
  let csv = 'Pillar,Question,Answer,Notes\\n';
  
  all.forEach(q => {{
    const ans = answers[q.id] || 'Not Answered';
    const note = (notes[q.id] || '').replace(/,/g, ';');
    csv += `"${{q.pillarName}}","${{q.title}}","${{ans}}","${{note}}"\\n`;
  }});
  
  const blob = new Blob([csv], {{ type: 'text/csv' }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'mindforge-assessment-' + new Date().toISOString().split('T')[0] + '.csv';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}}

function copySummary() {{
  const overall = calculateOverallScore();
  const posture = getPostureLabel(overall);
  
  let summary = `MAS MindForge Assessment Summary\\n`;
  summary += `Date: ${{new Date().toLocaleDateString()}}\\n`;
  summary += `Overall Score: ${{overall}}% (${{posture.label}})\\n\\n`;
  summary += `Domain Scores:\\n`;
  PILLARS.forEach((pillar, index) => {{
    summary += `- ${{pillar.name}}: ${{calculatePillarScore(index)}}%\\n`;
  }});
  
  navigator.clipboard.writeText(summary).then(() => {{
    alert('Summary copied to clipboard!');
  }}).catch(err => {{
    console.error('Copy failed:', err);
  }});
}}

window.MindForgeLens = {{
  answers: () => answers,
  calculateOverallScore,
  calculatePillarScore,
  getPostureLabel
}};
'''
    return js

# ============ FILE WRITING ============

def write_files():
    # Write HTML
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(generate_html())
    print("Written: index.html")
    
    # Write CSS
    with open("styles.css", "w", encoding="utf-8") as f:
        f.write(generate_css())
    print("Written: styles.css")
    
    # Write JS
    with open("app.js", "w", encoding="utf-8") as f:
        f.write(generate_js())
    print("Written: app.js")
    
    # Write README
    readme = '''# Unofficial Well-Architected MAS MindForge Lens

An interactive questionnaire and AWS Well-Architected Lens for the MAS Project MindForge AI Risk Management framework.

## Interactive Questionnaire

**Live Demo:** https://kdeath83.github.io/unofficial-wellarchitected-mas-mindforge-lens/

### Features
- 14 questions across 4 pillars
- Yes/Partial/No/N/A answer choices
- Real-time maturity scoring
- AWS native service recommendations per question
- Best practices and improvement plans
- Keyboard navigation (arrows, 1-4)
- Progress saved to localStorage
- Export to CSV
- Copy summary to clipboard

### AWS Services Mapped
| Pillar | Key AWS Services |
|--------|-----------------|
| AI Oversight | AWS Organizations, AWS Config, AWS Audit Manager |
| AI Risk Management | SageMaker Model Cards, Bedrock Guardrails, Security Hub, Macie |
| AI Lifecycle Management | SageMaker Clarify, CloudWatch, CloudTrail, Lambda |
| Enablers | AWS KMS, Secrets Manager, VPC, Training & Certification |

## AWS Well-Architected Lens

Download `mindforge-lens.json` and import into the AWS Well-Architected Tool.

## Deploy to AWS

| Service | Link |
|---------|------|
| **AWS Amplify** | [Deploy](https://console.aws.amazon.com/amplify/home#/deploy?repo=https://github.com/kdeath83/unofficial-wellarchitected-mas-mindforge-lens) |
| **GitHub Pages** | Already enabled |

## Local Development

```bash
git clone https://github.com/kdeath83/unofficial-wellarchitected-mas-mindforge-lens.git
cd unofficial-wellarchitected-mas-mindforge-lens
python3 -m http.server 8080
```

## License

MIT
'''
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    print("Written: README.md")
    
    # Write LICENSE
    license = '''MIT License

Copyright (c) 2026 Krish De

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
    with open("LICENSE", "w", encoding="utf-8") as f:
        f.write(license)
    print("Written: LICENSE")

# ============ GIT OPERATIONS ============

def git_operations():
    commands = [
        "git add -A",
        "git commit -m \"v1.1 - Interactive Well-Architected questionnaire with AWS service recommendations\"",
        "git push origin master --force"
    ]
    
    for cmd in commands:
        print(f"\nRunning: {cmd}")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(f"Exit code: {result.returncode}")
        if result.stdout:
            print(f"stdout: {result.stdout}")
        if result.stderr:
            print(f"stderr: {result.stderr}")

# ============ MAIN ============

if __name__ == "__main__":
    print("Building MAS MindForge Well-Architected Lens...")
    print("=" * 50)
    
    write_files()
    
    print("\n" + "=" * 50)
    print("Pushing to GitHub...")
    git_operations()
    
    print("\n" + "=" * 50)
    print("Done!")
    print(f"Repo: https://github.com/kdeath83/unofficial-wellarchitected-mas-mindforge-lens")
    print(f"Site: https://kdeath83.github.io/unofficial-wellarchitected-mas-mindforge-lens/")
'''

with open("build.py", "w", encoding="utf-8") as f:
    f.write(build_script)

print("Build script written: build.py")
