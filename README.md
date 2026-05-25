# Unofficial Well-Architected MAS MindForge Lens

A custom AWS Well-Architected Lens that maps the MAS Project MindForge AI Risk Management and Governance Framework (January 2026) into the AWS Well-Architected Tool.

**This is an unofficial, community-maintained project.** It is not endorsed by MAS or AWS.

---

## What This Is

The Monetary Authority of Singapore (MAS) Project MindForge provides a comprehensive AI Risk Management and Governance Framework for Financial Services Institutions. This lens translates that framework into the AWS Well-Architected Tool's custom lens format, enabling systematic AI governance reviews within AWS-native workflows.

---

## Live Site

https://kdeath83.github.io/unofficial-wellarchitected-mas-mindforge-lens/

---

## Lens Structure

| Pillar | Questions | Focus |
|--------|-----------|-------|
| **AI Oversight** | 2 | Scope, responsibilities, three lines of defence |
| **AI Risk Management** | 5 | Policies, enterprise risk, third party, use case, inventory |
| **AI Lifecycle Management** | 5 | Context/design, data, build/review, deploy, monitor/change |
| **Enablers** | 2 | Skills/knowledge/culture, infrastructure |

**Total:** 14 questions with risk rules, improvement plans, and best practices.

---

## Quick Start

1. Download `mindforge-lens.json` from the repo or the live site
2. Open the [AWS Well-Architected Tool](https://console.aws.amazon.com/wellarchitected)
3. Go to **Custom Lenses** > **Create custom lens**
4. Upload `mindforge-lens.json`
5. Review and publish
6. Apply to a workload and start your AI governance review

---

## Files

- `mindforge-lens.json` - The AWS Well-Architected Custom Lens definition (import this)
- `index.html` - Landing page with download button and import instructions
- `README.md` - This file
- `LICENSE` - MIT License

---

## Disclaimer

This lens is provided as-is for educational and assessment purposes. It is not a substitute for professional compliance advice. Always refer to the official MAS Project MindForge documentation for authoritative guidance:

- [AI Risk Management Operationalisation Handbook](https://www.mas.gov.sg/-/media/mas-media-library/schemes-and-initiatives/ftig/project-mindforge/mindforge-ai-risk-management-operationalisation-handbook.pdf)
- [Project MindForge Overview](https://www.mas.gov.sg/schemes-and-initiatives/ftig/project-mindforge)

---

## Related Projects

- [MAS MindForge AI Risk Assessment Accelerator](https://github.com/kdeath83/mas-mindforge-ai-risk-assessment-accelerator) - Interactive web-based checklist with scoring and gap analysis
- [EU AI Act Risk Classifier](https://github.com/kdeath83/eu-ai-act-risk-classifier) - Classify AI systems under the EU AI Act

---

## Contributing

Pull requests welcome. For major changes, please open an issue first.

---

## License

MIT - see LICENSE file for full text.

---

*Built by [kdeath83](https://github.com/kdeath83) · 2026*
